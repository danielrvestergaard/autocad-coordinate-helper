# import pyautogui
# import pyperclip
import numpy as np
import pandas as pd
# import re
# from pynput import mouse, keyboard
from ipywidgets import widgets
# from tkinter import filedialog, Tk

class AutoCAD_Coordinate_Helper:

    #coordinates = []

    def __init__(self):
        heading = widgets.HTML(
            '<h1>AutoCAD coordinate retriever</h1>'
        )
        explanation = widgets.HTML(
            '<p>1. Make sure your .dwg file is open in AutoCAD.</p>'
            '<p>2. Click the Launch button.</p>'
            '<p>3. Click the coordinates your wish to record.</p>'
            '<p>4. To exit coordinate clicking mode, right-click.</p>'
            '<p>5. You can delete selected coordinates by using the Delete button.</p>'
            '<p>6. You may re-enter clicking mode by clicking the Launch button.</p>'
            '<p>7. Click the Save button to export the coordinates to a .csv file in your selected folder.</p>'
        )
        display(heading)
        display(explanation)
        
    #     launch_button = self._launchButton
    #     save_button = self._saveButton
    #     delete_button = self._deleteButton
    #     self.select = self._select

    #     left_box = widgets.VBox([launch_button, save_button, delete_button])
    #     right_box = widgets.VBox([self.select])
    #     box = widgets.HBox([left_box, right_box])
    #     display(box)
        
    #     # display(launch_button)
    #     # display(self.select)
    #     # display(delete_button)
    #     # display(save_button)

    # def on_mouse_click(self, x, y, button, pressed, injected):
    #     if pressed:
    #         # Do nothing while pressed
    #         pass
    #     else:
    #         # Upon release:
    #         if button==mouse.Button.right:
    #             #listener.stop()
    #             return False
    #         else:
    #             # Copy command history to clipboard
    #             pyautogui.typewrite('copyhist')
    #             pyautogui.sleep(0.1)
    #             pyautogui.press('enter')
    #             pyautogui.sleep(0.1)
    #             tmp = pyperclip.paste()

    #             # Extract coordinates
    #             pattern = r'X\s*=\s*(-?\d+\.?\d*)\s*Y\s*=\s*(-?\d+\.?\d*)\s*Z\s*=\s*(-?\d+\.?\d*)'
    #             input_string = tmp.split('\r\n')[-3]
    #             matches = re.findall(pattern, input_string)
    #             if matches:
    #                 self.coordinates.append(matches[0])
    #                 self.select.options = [ ', '.join(xyz) for xyz in self.coordinates ]

    #             # Get ready for next click
    #             pyautogui.sleep(0.1)
    #             pyautogui.typewrite('id')
    #             pyautogui.press('enter')

    # def myfun(self, b):
    #     # MAKE INITIAL COMMANDS
    #     window = pyautogui.getWindowsWithTitle("Autodesk AutoCAD")[0]
    #     window.maximize()
    #     pyautogui.click(
    #         window.topleft[0]+0.5*window.width,
    #         window.topleft[1]+0.01*window.height
    #     )
    #     pyautogui.sleep(0.1)
    #     pyautogui.typewrite('id')
    #     pyautogui.press('enter')

    #     # Collect events until released
    #     with mouse.Listener(
    #        #on_move=on_move,
    #         on_click=self.on_mouse_click,
    #        # on_scroll=on_scroll
    #     ) as listener:
    #         listener.join()

    # @property
    # def _launchButton(self):
    #     button = widgets.Button(
    #         description='Launch',
    #         disabled=False,
    #         button_style='', # 'success', 'info', 'warning', 'danger' or ''
    #         tooltip='Launch',
    #     )
    #     button.on_click(self.myfun)
    #     return button

    # @property
    # def _saveButton(self):
    #     button = widgets.Button(
    #         description='Save',
    #         disabled=False,
    #         button_style='', # 'success', 'info', 'warning', 'danger' or ''
    #         tooltip='Save',
    #     )
    #     button.on_click(self.save_coordinates)
    #     return button

    # @property
    # def _deleteButton(self):
    #     button = widgets.Button(
    #         description='Delete',
    #         disabled=False,
    #         button_style='', # 'success', 'info', 'warning', 'danger' or ''
    #         tooltip='Delete',
    #     )
    #     button.on_click(self.delete_coordinate)
    #     return button

    # def save_coordinates(self, folder_path):
    #     root = Tk()
    #     root.withdraw()

    #     # Ask the user to select a folder
    #     folder_selected = filedialog.askdirectory()
    #     df = pd.DataFrame(np.array(self.coordinates, dtype=float),
    #                       columns=['x', 'y', 'z'])
    #     df.to_csv(folder_selected+r'/'+'coordinates.csv', sep=';', index=False, )

    # def delete_coordinate(self, b):
    #     remove_indices = set(
    #         [ self.select.options.index(value) for value in self.select.value ]
    #     )
    #     all_indices = set(
    #         [ idx for idx in range(len(self.coordinates)) if idx not in remove_indices ]
    #     )
    #     keep_indices = all_indices.difference(remove_indices)
    #     self.coordinates = [ self.coordinates[idx] for idx in sorted(list(keep_indices)) ]
    #     self.select.options = [ ', '.join(xyz) for xyz in self.coordinates ]

    # @property
    # def _select(self):
    #     select = widgets.SelectMultiple(
    #         options=[ ', '.join(xyz) for xyz in self.coordinates ],
    #         value=[],
    #         #rows=10,
    #         description='Coordinates',
    #         disabled=False
    #     )
    #     return select
