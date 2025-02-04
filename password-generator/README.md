# Secure Password Generator

A CLI tool to generate cryptographically secure passwords with customizable rules.

## Features
- Guaranteed inclusion of uppercase, lowercase, digits, and special characters
- Optional exclusion of ambiguous characters (`l`, `1`, `O`, `0`)
- Configurable length (minimum 4)

## Usage
```bash
python password_generator.py [--length 16] [--exclude-ambiguous]

# Generate a 20-character password without ambiguous chars
python password_generator.py -l 20 -x


---

### **Step 4: Test Edge Cases**
1. **Minimum Length**:
   ```bash
   python password_generator.py -l 4
   # Output: e.g., "Kd3$"

   python password_generator.py -x
# No 'l', '1', 'O', or '0' in output

python password_generator.py -l 25

