import sys
import os

# Add root directory to the import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main

if __name__ == "__main__":
    main.app.run(host='0.0.0.0', port=5000)