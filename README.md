# ConsoleMasterPy
ConsoleMasterPy is a Python library that simplifies console manipulation on Windows systems. It provides functionalities for changing console colors, hiding/showing the cursor, setting console window size, and more.

## Installation
You can install ConsoleMasterPy using pip:
```bash
pip install ConsoleMasterPy
```

## Usage
```python
from ConsoleMasterPy import ConsoleMaster
```
### Create a new console window
```python
console = ConsoleMaster(title="My Console", font_size=17, window_width=30, window_height=25)
```
### Change console colors
```python
console.change_console_color(background_color=(0, 0, 0), foreground_color=(255, 255, 255))
```
### Print with custom colors
```python
console.print_with_color(rgb_background=(0, 0, 0), rgb_foreground=(255, 255, 255), element_to_print="Hello, World!")
```
### Change console window size
```python
console.change_windows_size(width=40, height=30)
```
### Hide the cursor
```python
console.hide_cursor()
```
### Pause execution until user input
```python
console.pause()
```
### Go to specified position (x, y) in the console window
```python
console.go_xy(x=10, y=5)
```
### Change pixel size of the console font
```python
console.change_pixel_size(size=20)
```
### Clean a specified zone in the console window
```python
console.clean_zone(x_coord_init=5, y_coord_init=5, x_coord_end=15, y_coord_end=10)
```
### Clean the entire console window
```python
console.clean_windows()
```
### Pause execution until user input
```python
console.pause()
```

## Additional Functions
### generate_name()
This function generates a random name with a mix of vowels and consonants.
```python
from ConsoleMasterPy import generate_name

name = generate_name()
print(name)
```

## `exception_handler` Function

The `exception_handler` function is a decorator used to handle exceptions within functions. It catches any exceptions that occur during the execution of the decorated function and logs the error message, along with a timestamp, to a file named `log.txt`. This decorator ensures that the program can continue running smoothly even if an exception occurs, providing better error handling and debugging.

### Parameters

- `func`: The function to be decorated with exception handling.

### Example Usage

```python
@exception_handler
def my_function():
    # Code that might raise an exception
    pass
```

## Example usage - Game of Life of John Horton Conway
```python
from ConsoleMasterPy import ConsoleMaster, exception_handler
import random
from time import sleep

def copy_matrix(matrix):
    return [row[:] for row in matrix]

width, height = 35, 35
console_manager = ConsoleMaster("GAME OF LIFE", 13, width, height)

@exception_handler
def main():
    generation_counter = 0
    
    while True:
        if generation_counter == 0:
            current_matrix = [[0 for x in range(width)] for y in range(height)]
            next_matrix = copy_matrix(current_matrix)
            cell_color = [random.randint(0, 255) for _ in range(3)]

            live_cell_rules = [random.randint(0, 1) for _ in range(9)]
            birth_rules = [random.randint(0, 1) for _ in range(9)]

            for x in range(width):
                next_matrix[x][0] = 0
                next_matrix[x][height - 1] = 0
                next_matrix[x][1] = 1
                next_matrix[x][height - 2] = 1

            for y in range(height):
                next_matrix[0][y] = 0
                next_matrix[width - 1][y] = 0
                next_matrix[1][y] = 1
                next_matrix[width - 2][y] = 1

            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    cell_value = next_matrix[x][y]
                    console_manager.go_xy(x, y)
                    color = cell_color if cell_value else [0, 0, 0]
                    console_manager.print_with_color(color, [0, 0, 0], " ")
            generation_counter = 300

        generation_counter -= 1

        current_matrix = copy_matrix(next_matrix)
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                neighbors = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]
                count = sum(1 for i, j in neighbors if 0 <= i < width and 0 <= j < height and current_matrix[i][j] == 1)

                if current_matrix[x][y] == 1:
                    if not live_cell_rules[count]:
                        next_matrix[x][y] = 0
                        console_manager.go_xy(x, y)
                        console_manager.print_with_color([0, 0, 0], [0, 0, 0], " ")
                    else:
                        next_matrix[x][y] = 1
                else:
                    if birth_rules[count]:
                        next_matrix[x][y] = 1
                        console_manager.go_xy(x, y)
                        console_manager.print_with_color(cell_color, [0, 0, 0], " ")
                    else:
                        next_matrix[x][y] = 0
        sleep(0.05)

main()
```

## License
### ConsoleMasterPy is licensed under the MIT.