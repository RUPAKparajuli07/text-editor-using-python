# Notepad Application Documentation

This document provides documentation for a simple text editor application created using the Python Tkinter library. This application is a basic text editor similar to Windows Notepad, allowing users to open, edit, and save text files. Additionally, it provides options to format text with bold, italic, colors, and highlighting.

## Table of Contents
1. [Introduction](#introduction)
2. [Functionality](#functionality)
3. [Usage](#usage)
4. [Code Explanation](#code-explanation)
   - [Import Statements](#import-statements)
   - [Function Definitions](#function-definitions)
   - [Main Application Window](#main-application-window)
   - [Text Editor](#text-editor)
   - [Formatting Buttons](#formatting-buttons)
5. [Conclusion](#conclusion)

### 1. Introduction <a name="introduction"></a>
This Notepad application is a graphical user interface (GUI) program developed using the Tkinter library, which is the standard GUI library for Python. It allows users to create, open, edit, and save text files, as well as apply various text formatting options such as bold, italic, colors, and highlighting.

### 2. Functionality <a name="functionality"></a>
The Notepad application offers the following functionality:

- **Open File:** Users can open an existing text file for editing. Supported file types include text files (*.txt) and all files (*.*).

- **Save File:** Users can save the current text as a new file. The application provides the option to specify the file name and file type (default is *.txt).

- **Text Formatting:** The application includes buttons to format the selected text within the text editor. Users can apply bold, italic, different text colors, and text highlighting to selected portions of text.

### 3. Usage <a name="usage"></a>
1. Run the Python script.
2. The main application window will open, providing you with the Notepad interface.
3. Use the "Open" button to load an existing text file for editing.
4. Use the "Save As" button to save the edited text as a new file.
5. To format text, first select the text you want to format within the text editor, and then click one of the formatting buttons (Bold, Italic, Red, Blue, Green, Highlight).

### 4. Code Explanation <a name="code-explanation"></a>

#### Import Statements <a name="import-statements"></a>
- The application utilizes the Tkinter library for GUI development. It also imports `tkFont` for font manipulation and `askopenfilename` and `asksaveasfilename` from `tkinter.filedialog` for file-related functions.

#### Function Definitions <a name="function-definitions"></a>
- `open_file()`: Opens an existing text file for editing. It uses the `askopenfilename` function to display a file dialog for selecting a file and loads the selected file's content into the text editor.

- `save_file()`: Saves the current text as a new file. It uses the `asksaveasfilename` function to display a file dialog for specifying the file name and type and saves the text to the selected file.

#### Main Application Window <a name="main-application-window"></a>
- The main application window is created using `tk.Tk()`. It includes settings for the window title, row and column configurations, and weights to ensure the widgets expand with the window.

#### Text Editor <a name="text-editor"></a>
- The text editor is created using `tk.Text` and uses a default font style, size, and family. It allows users to input and edit text.

#### Formatting Buttons <a name="formatting-buttons"></a>
- The application provides buttons for applying formatting to selected text within the editor. This includes options for making text bold, italic, changing text color (red, blue, green), and highlighting text.

### 5. Conclusion <a name="conclusion"></a>
This Notepad application provides a basic text editing environment with support for text formatting options. It serves as a starting point for more advanced text editor projects and can be further customized and extended to meet specific requirements. Users can open, edit, and save text files with ease, making it a handy tool for various text editing tasks.
