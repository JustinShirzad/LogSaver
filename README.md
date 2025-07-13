# LogSaver
- Create simple logs for your Python project.
- Uses process names and timestamps to automatically create and write to a log file.

## Installation
```bash
git clone https://github.com/yourusername/LogSaver.git
cd LogSaver
pip install -e .
```

## Quick Start
```python
from logsaver import LogSaver

# Create logger
logs = LogSaver()

# Log messages
logs.I("Process started")           # INFO
logs.W("Low memory warning")        # WARNING  
logs.E("Connection failed")         # ERROR
logs.D("Debug information")         # DEBUG
logs.C("Critical system failure")   # CRITICAL

# Or use full method names
logs.info("Process completed")
logs.error("Something went wrong")
```

## Output Format
```
[ INFO ] : 14:30:45 12-07-2025 : my_script - Line 11 : Process started
[ ERROR ] : 14:30:46 12-07-2025 : my_script - Line 12 : Connection failed
```

## Configuations
**Change process and file name**
```python
process_name="demo"
```

**Change folder directory**
```python
log_dir="logs"
```

**Toggle showing timestamp**
```python
show_timestamp=True
```

**Toggle showing level**
```python
show_level=True
```

**Toggle showing process name**
```python
show_process_name=True
```

**Toggle showing line number**
```python
show_line_number=True
```

```python
# Example
logs = LogSaver(log_dir="hello", show_timestamp=False)
```

### Future Plans
- None at the moment
