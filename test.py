def test_js_line():
    js_line = "const http = require('http')();"
    
    # Check if there is a syntax error
    try:
        exec(js_line)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
    except Exception as e:
        print(f"Error: {e}")

test_js_line()
