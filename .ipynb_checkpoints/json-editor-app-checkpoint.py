import streamlit as st
import json
from pathlib import Path
import copy
from typing import Any, Dict, List, Union

def flatten_json(nested_json: Dict[str, Any], parent_key: str = '', sep: str = '.', level: int = 0) -> Dict[str, Any]:
    """Flatten a nested JSON object while preserving type information and level."""
    items = {}
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        
        if isinstance(v, dict):
            # Store the dict itself at this level
            items[new_key] = {
                'value': v,
                'type': 'dict',
                'level': level
            }
            # Also store all nested items
            items.update(flatten_json(v, new_key, sep=sep, level=level + 1))
        elif isinstance(v, list):
            items[new_key] = {
                'value': v,
                'type': 'list',
                'level': level
            }
        else:
            items[new_key] = {
                'value': v,
                'type': type(v).__name__,
                'level': level
            }
    return items

def unflatten_json(flattened_dict: Dict[str, Dict[str, Any]], sep: str = '.') -> Dict[str, Any]:
    """Convert flattened dictionary back to nested JSON while handling type information."""
    result = {}
    # First pass: handle non-dict values and create structure
    for key, value_info in flattened_dict.items():
        if value_info['type'] != 'dict':  # Skip dict types for now
            parts = key.split(sep)
            target = result
            for part in parts[:-1]:
                target = target.setdefault(part, {})
            
            # Convert value based on type
            raw_value = value_info['value']
            if value_info['type'] == 'int':
                try:
                    raw_value = int(raw_value)
                except ValueError:
                    raw_value = 0
            elif value_info['type'] == 'float':
                try:
                    raw_value = float(raw_value)
                except ValueError:
                    raw_value = 0.0
            elif value_info['type'] == 'bool':
                raw_value = str(raw_value).lower() == 'true'
            elif value_info['type'] == 'list':
                if isinstance(raw_value, str):
                    try:
                        raw_value = json.loads(raw_value)
                    except json.JSONDecodeError:
                        raw_value = []
            
            target[parts[-1]] = raw_value
            
    return result

def render_value_editor(key: str, value_info: Dict[str, Any], on_change: callable) -> None:
    """Render appropriate editor for different value types with indentation."""
    indent = "  " * value_info['level']
    display_key = key.split('.')[-1]
    
    # Calculate a reasonable width based on content
    content_length = len(str(value_info['value']))
    min_width = 400
    max_width = 800
    width = min(max(content_length * 8, min_width), max_width)
    
    if value_info['type'] == 'dict':
        st.markdown(f"{indent}📁 **{display_key}**")
    elif value_info['type'] == 'list':
        # Calculate dynamic height for list content
        list_content = json.dumps(value_info['value'], indent=2)
        num_newlines = list_content.count('\n')
        content_length = len(list_content)
        calculated_height = max(68, (num_newlines + 1) * 20 + (content_length // 50) * 20)
        height = min(400, calculated_height)
        
        st.text_area(
            f"{indent}📝 {display_key} (list)",
            value=list_content,
            key=f"input_{key}",
            height=height,
            help="Edit as JSON array",
            on_change=on_change,
            kwargs={'key': key}
        )
    else:
        if isinstance(value_info['value'], bool):
            st.checkbox(
                f"{indent}🔘 {display_key}",
                value=value_info['value'],
                key=f"input_{key}",
                on_change=on_change,
                kwargs={'key': key}
            )
        elif isinstance(value_info['value'], (int, float)):
            st.number_input(
                f"{indent}🔢 {display_key}",
                value=float(value_info['value']),
                key=f"input_{key}",
                on_change=on_change,
                kwargs={'key': key}
            )
        else:
            # Calculate dynamic height based on content (minimum 68px as per Streamlit requirement)
            num_newlines = str(value_info['value']).count('\n')
            content_length = len(str(value_info['value']))
            # Base height calculation: ~20px per line + extra space for long content
            calculated_height = max(68, (num_newlines + 1) * 20 + (content_length // 50) * 20)
            # Cap the maximum height
            height = min(400, calculated_height)
            
            st.text_area(
                f"{indent}📝 {display_key}",
                value=str(value_info['value']),
                key=f"input_{key}",
                height=height,
                help=f"Type: {value_info['type']}",
                on_change=on_change,
                kwargs={'key': key}
            )

def update_value(key: str):
    """Update the value in session state when input changes."""
    input_key = f"input_{key}"
    if input_key in st.session_state:
        st.session_state.edited_data[key]['value'] = st.session_state[input_key]
        st.session_state.modified = True

def main():
    st.set_page_config(layout="wide")
    st.title("JSON Editor")
    st.write("Upload a JSON file, edit values, and save the modified version")

    # Initialize session state
    if 'modified' not in st.session_state:
        st.session_state.modified = False

    # File uploader
    uploaded_file = st.file_uploader("Choose a JSON file", type=['json'])
    
    if uploaded_file is not None:
        # Load and parse JSON
        try:
            json_data = json.load(uploaded_file)
            if 'json_data' not in st.session_state:
                st.session_state.json_data = json_data
                st.session_state.flattened_data = flatten_json(json_data)
                st.session_state.edited_data = copy.deepcopy(st.session_state.flattened_data)
        except json.JSONDecodeError:
            st.error("Error: Invalid JSON file")
            return

        st.subheader("Edit Values")
        # Sort keys by level and then alphabetically
        sorted_keys = sorted(
            st.session_state.flattened_data.keys(),
            key=lambda k: (st.session_state.flattened_data[k]['level'], k)
        )
        
        # Create input fields for each value
        for key in sorted_keys:
            value_info = st.session_state.edited_data[key]
            render_value_editor(key, value_info, update_value)

        if st.session_state.modified:
            # Convert edited data back to nested structure
            try:
                modified_json = unflatten_json(st.session_state.edited_data)
                #st.json(modified_json)

                # Save button
                json_str = json.dumps(modified_json, indent=2)
                st.download_button(
                    label="💾 Download Modified JSON",
                    data=json_str,
                    file_name="modified.json",
                    mime="application/json",
                    key="download_button"
                )
            except Exception as e:
                st.error(f"Error processing JSON: {str(e)}")
        else:
            #st.json(st.session_state.json_data)
            st.info("No modifications made yet.")

if __name__ == "__main__":
    main()