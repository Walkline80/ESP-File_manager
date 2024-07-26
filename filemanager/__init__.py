index = r'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible"content="IE=edge,chrome=1"><meta name="viewport"content="width=device-width, initial-scale=0.80, maximum-scale=1.0, user-scalable=yes"/><meta name="mobile-web-app-capable"content="yes"><meta name="apple-mobile-web-app-capable"content="yes"><title>MicroPython File Manager</title><link rel="stylesheet"href="styles.css"></head><body><div class="file-manager"><div class="toolbar"><input type="file"id="file-upload"style="display: none;"multiple><button id="upload"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAADb0lEQVR42q2Va2gUVxTH/3dmdxMza8QQrRa0VFGjNEWzVCIENz4aX6C2H6wWRD8KVQpRCxUfQRDU2hbRD2o+iFqqtPUVo2ts89iqNRojLT7S7NZHTNwYsxs3j83uZmbu6ZkNSARFs+uB4V7m3vv/3fOYMwIpWJGnnYQCVMwbIV63RwxGcKAVlrfThmkaasMmahqjuPL5yFdqJQWYWfaMilncnmZHU1zC+6AHjx5HcX3lGJEywH36Ka1zDcUopwNXwwZsHKJ0m8C5W8/xLBDFrTXjRNIA15EWWvpxBmZ/4ERVB4sTYBJB8ihZyuNtRaw7jn/WTxGDBuSWNtEXeUNRMNaJypAOhYVNC8DqpuQN1lwFqioDiHVG0bB1qnhrQN7Bh/QZhyXnvQyUP4kjN8uBll5WTUDYA4b0xEzE+J0uBBouN0Pvi+O/nfnijYC8/X6yxj5DwtBN9Pbo+O2riThwPwaFj5t8fVIEfPfCCNxphcKuCOuRlFySx35bT8e+zsHexjjsfHudhawItTQ+R+huAA/3u5NPsmXvF9fS4Y0fYfffEdj4uOREGPw+6OtAV0MATaVzUgOMWuOlQ5tc2FHXBc4pDAaYLNPpCyLua0bz0UWpAUau/p32leRj859hOPh0X5+EVAVi/iDo/mMETixNDZC9/ALt2ePGN54Q7Gp/iEzitPpb+XmE4JllqQGw8CyNn5SFpjtPYVdkooosk8RVFuP51ZUvA8rOVwyRUm6VRPG30eeKlJoDEf4GdEVR6MUV+0dFSqRH4kjneTqvbxe/niprn/GJK1vlpkI0aH8GhEJwX7InRpMMGIaOv+rqg+La9ZuUP92VvPIAq2urRigaQsHo+XCmOVF7ox6iuvoyFRYWMNFIWlgVKtoibdhyezEyhwSRS9uw2rUKNTVXIC5UVFLRnJlcbnpKgEB3AAtPTsaI0RqWaCUonrsWnktVEKfOlFPRp7Oh6zqE1Zre3J5eEX/AoabB3+bnxgd8mD0GdocDFy/9AfHT8V9owby56OgIo6e7G0JRkvLCgijsiVWumqZheNYweCoYUHr4CM1yu+Hz+3Gv4V+oqpp0qCwzTRNTJudg4oQJqPZ6IXZ99yN9uWJ5Islct/1hSsEo8X+QsNls+Pn4CYhNm0u+1zK04sxhmYnFd2HWJbs6uxDpjfzwP0ptjebUDXW8AAAAAElFTkSuQmCC"class="icon"><span>Upload</span></button><button id="download"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAADUElEQVR42q2WeUgUURzHv29mV/PIyogsSvJIsyhIiIKC/gmiA4yKLlDsMLAQOiCsrMzIJOmwQ8gOyY0tSoOK7iLCSq0gCaLLdbPMat3c1s3Zddd5v96MWNG9u/2GmXkwP76f3/GOYfjBJlUm0aRhqWCqBK4CnANql3hAxtXa+3iS+5LBD/vJebw5jo5NLcDJlg3iYxg0bcYYbO1AzR3+fwAHp2yF+c0WyCwcKnU7tWqAax683GEJDjDywFAqn7cdpqZuABGDqBTa2gkPb/wHQFLxEKpIL8TRpnwYezIgCa1OFY+uuNG4pzE4QHzBYDItL8Jhaz4MiOgGCK+PDo7HlxRYD1j9A4wtGU7aICqiLxwOF2w2B6rW7EOpJU+UqJcoEfT7Y5uK+qoOGIyAJAuG2i3QdPTVH4H6x9E7Eyg6agCK56+A+XUJWlxOhECIcwaNroo+MIlBDiW4FMBS64bzhRfNx5r+ms1Xh8QNsRQbG4+NaZk4bCkC75JFaWQ9eq49RNSdPkLjAw+cT4X48b+L/9SD2JwhNCwhAavmpuGEpUyE3gMRbgbg+T0FjsdetJj/TfyXTR6YEUOJo5KwetEsVDSUiRmkFV1CQ63/4r8E9EDikodjdcZsmBqOwFrnRVu9gnen3vol/luAZuFzIik1dRwccjOsNe+hnHP5Lf5HgG4zGYkOA5cQkPhXwJmz59dyTlFiqK8JSZIo3BjeKYaq4lPCOOeSv8KSxEKFTgE7XXnuTnJy4sT+0X3FbKFAA9V3XAMz6m+VuuD1+lBT99DOyitOUmb6goCFv7ealuuwu+2YPHg6osL6oPpuHVhpWTllZ2XC5/MFLCyLtfLu81vk1c9CZIQdY9Q8ZE3IwvUbt8D27j9EOSuXwe32BAVo/vQGM6pGITqmF9IitiB32hpcuHwFrGhXCeVkZ8Hj6dTrp92BWKgcimcfnotjlhA/IA4hIUZcvHwVbFthMWUvX4x2Vwfsra3aDAosDRGYlgknjsjekejXr48AXAPblF9IGekLYftgw+3qahi0/TgIU8WfQkpKClJGJOHmTdGD9es305Kli/VDRZbkgEvUYyQuVeUwGg0wmcxg63I3ZQvJ0phBMeIXhQcl/q1aDJ+cTigdyu4v2t9o/QyvG+QAAAAASUVORK5CYII="class="icon"><span>Download</span></button><button id="move-to"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAD4klEQVR42q2Ue0jTURTHz91va6ZGaVb0sDKDuaQ0H5SZShoULkLLSBu9ZtEfZZYJRfR+EJKE0YOKgjSh1HKW2vKJJmkay6Y9ltUsZoZUaq093Nzvdn/b/OEa6qwO7Pfbj3u+53POvedcBKOwldL3VV0acGneNDfcWQ1y1lEkfVeSGeMj6tBjSCtRVbUmC5b/N4DgkrIwO8k3vr0PQ6cRwN8FIL1YVfpym9+qfwZ4Z7ReyJUIdn02YfhoQEABBopDoGMBjj1Q3ZRvF279awAJfvZasiDdYEag+kVDH0IWASYPPoH48jGkZLddVO+fnzJqgG+Ggk+S/aAzwnTm+6JECK06DByi4BDQldtvLH58HlIDwsIP+wO0TgN8jsvd2o8Gs4KpJxQ4S+IHLzRke4iCIpQbeUroOByAhtIMCZh2sKmG4qIQ9YlQ98GAzM0CaP6JgWsDZN97aweYebipG9OoQn06dP2QAMFp+aNDYr8VqVkt0J0VhgYDzhDA8x6areBOUZsdIPDySxwUPBtqZMp81bGQ9Q4A70ONVZd2zI/uMlNwJEfpsG3HxaSCXrMFwJxBYck78PKkLGfCGE1+0RG+0Ks1waN8xb3OcxEJLGDKvvrKyymBMW1kiNQ6GgLGcwFjq5B5Mf87DTR0kTUmICNCTEcNqt/iR2NAxEHbR0NloRWCpqXV1Z5PDYpUahG02TKkATt2A+lNDgdGNqZC8tIZaagtUMiQ/8mG5r3iwMDSTyZwoUZxdwzHIKVhkumTBy1qS7yAU421CfHzIhXfMcmeOUhkR8I0s03YIQgaXBEe8EFgNNHwvPz1p46M8NlsGC9JWdWBtLDox18xvMqrBx6PAopUZO6nwWQyg3BdOAthgtedf+iQeVS6CPQaEzTfbWr9djN2gUObTt5eVr1z99Jlt7Ll8D4zkl0TppZjb1Eo0GYrgEPKb7wggx/FG1if8QlFOHhLBLTkN8q+5cTGOrTpgM1KqZZPcB8TpDizlF1bkFaBPaIXArYBEAG8uFpuB/BMvP+drNf2FMSt+ePMHc0jqcit53YcO/b+e8rxuGXBgPtpq4jLgTfXy+wAf2qGBVhKji9wmzpnovrL2y8eXjM8YVxMCKnABiD3dXtOhdWRx9OTA570Q7rO+ctuwGYml97nRwWt5oyhrNkPdBLTQVwK+ru18FX29OnP4sSwoWKM2Pbuq/NyPVcuFiNXHplAG4BMK02uhN7KZzKNNCF2OL1Tc+W6IjfHPS5qI3CtjY+0RtCU1TfoZOIlI2mdHtyxawtvuMYskoC+D7Syuo+Gys0+zuhGdTPwRXekSK8LMVRLvJ3V/AbpNJxnTgyfxgAAAABJRU5ErkJggg=="class="icon"><span>Move To</span></button><button id="copy-to"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAEhElEQVR42p2Ue2xURRTGv9m72+3DYNPwVGOKwfqPiZIo+AiiUSqlKglVjMHyqDx9gK0KhcQ/eFhiUwgRIyg21WJMqTYxQltoCN0YQkOKJAYhSmsskZK2lG73vu/cl2fu2oWGgltmM7vJ7Jn5zTnfN4dtb4j5rzw2AwOKCdPk0LmFuGFhWHMQVzQMyArq1r/KcIeD1cfOOqVzZ0qAR4dakGkOqxb65QQGhznO9fbh4uVBNFW+cUcQVnvsNC8rnBVxHQea40LWXRi6RjAD13QbZ7quIH9iDtp+68HBipJxQ9iXLaf56iICuC5834PpAqqiQjYcqKaNzq5ezJiSh8ysCPYf7cR3H4yvXGzfkQ6+tvgJAnB4Hu1lPjSbpmHDcx383PEHygpn4lJ/Ap3dvWg+241DGxenDWGfHTnF3yt+kgAOAfxgUXB07sG2ORpj59EnqyiYmotpk3LBCXxV0ymWTKA7SGgcQ7qKq3EFjZuW3ARmu5t+4eWL5gQlcjwPIVoU0w0xaNyFWP/h5Dmsmz9boKGSLrJuYJgOv0ZGuBI3EZcNdPx9CVcHNLRuXzYKwnY1xXjForkR13dhOR4i/wHEl+0w2MxBbWsn3l84h0rmkhEIoPowLINgemDvIXLe6T978dSDk3Dmrz5Uly1IQVhVwwm++fXnIprlwKUbin8yQxI8EjwkMUSkEGqaTuLDkmdw3QgMuqZCoWzi9F4Sqo4OMsOqFx6hsnGc+L0H7xTPCiCssu4Y37m8MBIn74vNYoSpPBKlwKIMWeEIqhtj2LT4WYwYgdFWzXYDIxh0Mc20cOrCJaxe8DgGrilo+bUb7ed7Asexym8JsFQAzBRASB1mIcpAQlYmAX6MYctr1wEjRhAQkyCmZaHniozL8SEMxC0kKE4j8Y+fvQi2ub6NV5XOGwUIUmMsmNkZGfiksR1blzwflMjzkjECQ5WCRRDZdMBNEwrBZJmjn96R6zvY+n37rQEj4y4CbGtox45l8wIA95JG8FMQhoTB4ZL4Ot1aoWwGEyZCYYZ1nx/+f0BmRgQ7Dh1H1dIisnESIA6P+tdjPEpF9XXoisjIwJDCMSEnCy9tqwf7+GAb3/bm2ABxRkZUwpa649i7pphKYcMnSAAIhemXPmHSS0DI0go9TJtiRB+bmnc3ZpfvA9twoIXvWVkUEZ3UuQEQEu+AHBKWIqj8phkH1pfQ4zLptskM6DZ0sIQMMoIdRVA2Rpko1PJVKtn0ybl4YGUNWMWBZn/XygW37Sdv7z+ML9a+nALcOCR6JyGRg0RYN2kOmXS4JzcH01cQ4P7Snf7D+ffCJgHHGqI/PVowFTUrisYEhMOUge0gGo4GJRPSC8FzJ2QhXwDS6Ygf1R31q5e/OCYgBRK9RUrqRkphYvY4AOW1Lf7usqLbApwUiACkz5QJOekDNhLg01sAxAEO1V20byGDJEQn2uTc7PQBq/b+5H/17sLAfqbr3bTJ0C1aS/pVdGKDCAXT8sahwdetfvVb89MJHTUeWrMnPQCe3uDflz8F3HHTChcjSh3gnwtd+BfdcMKtmD5yQwAAAABJRU5ErkJggg=="class="icon"><span>Copy To</span></button><button id="rename"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAA4UlEQVR4nO3VsUqCURQH8J+BjkHPIG5JtDeGClK7LmU9gaNLky9gkIs6uAZNNbS4+ATfZg9Qr+AcX1zhG1Lw0wsF/uFc7uUczv/cc7nnzx/DMaZ4xE04r1BFD2N08hIcoYk7TPCJGob4wANaqOznPpxjiRlKIuEN1yLiBY1NAWVc5rCLDEFvTUyaWx8Jnre0pwzB/Bd/EnL/LN0ILeoeCFY4tOiftCiJ+dHKsUdF9GG3K15xJRJOg+C8o7iPhAXUcR+09ytUn+4XQTLbu0hmWuUIA9ziJOM7C4+d+nOL/tb4BgGwWoYIo69tAAAAAElFTkSuQmCC"class="icon"><span>Rename</span></button><button id="new-folder"><img src="data:image/png;base64,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"class="icon"><span>New Folder</span></button><button id="delete"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAFKklEQVR42pVWWW8TVxg9d8aOPbZjx453B0JIIZBAgCDUSqiqRCWiRkDpQx9aQR/av9X2gT5ULUWiTcvSiFaqxEM3oAHSkDRkdeIltjNeYjuema/fzLiILRSudSVLvvec75zvfDMW4LWe2E1SqAvC64FRKMKo1RHJzAu8wsrH+0jyKpC6Q3Wq1RSjqCK89lCIXHI3OY8cgHvsTYigD/rsChqXb0BPryGaW3wpkly0l+RUAu6zb0PekwIVKmhcu4nW7XsQ+aERUs6PQVAJpG5ASvWCthTUL4yXtEw2GM++mCTD4I5EjJSPTgvRUYeRXoIIBEBSkDGuQOSOHNOUdw7JVFgGDMaSBFcxCNL9qH76TcUolzuT25CkbfCq9/wZn1mg/s8UYxBjELuRRP3aXV2kewfIPZxAR48HZPAt4gP8RX5tPzTVidrXV0uaqgZ35pefIFkK7yBnKlHynTsVlIw2uJB4CwhZQnMmj8ZUHmIxtouEUyJlOCHcPZ2MTW0SYiVDaKkyKpeuM0k52JdbskjmIzvJGY+V/OfGgrKhQp+5bym3wQUayxXU72ZALYMJkruFbpAhOSR4D0TgSvltEnPDVDIIQw5h46vr9VZ6VTGJnamk3vXhmCxr69Bm7MqFJIGYo/5PEfU57qfOdyUhPZI9aypxSNQ5FBFKsvMxEoKDe6K5wqj8/Aeo0YR/9Djk1jonjisH28KWmEDV2SJqc0VLTH9mwcJ+wtdpm8QI7AtLnqS3bZcphKvhdEl9A+yCgL44C335oV25EBaKOreB2nzJAhxogz9DYK77nAywXcGBEHxxH2MbbRIdwuOzfKZahQuXrdsmQXmxDPXhhlX54GPgzyUw12SMSSRhdO8NSb6Ix+q5tZjEWiY4LC5U8zUUHpSsIoazC8/gbTtEf5pJccmUPBgRTsVh2/XUTeKupv/KolnZwtH15edibUvwa3cPKakY9ewNCKlZ4QKlJw/wrAjFi5WZMmorObxeWHl5gpvBBLl7UsaOk29IrqV74GlmW54m4Gl1udDsG8bKxG9orK7ieCnz/xb9EoyRO5FA75kT8OQXoS3MtT0nOzEWNtlXDY0jvB9VXwwLF69iSy3jrY3M9k3+icGVRMzof29U8mQX0TKHyOG0wfmj64Z1TubcE9o94d44Bg+iJPmxOD6BVrmCE48pefRloitqVk57zo4KXzGNrclJa/zNqs3Ci+Um1tY3rbOJsAchv6v9RGFyjrJz+DAKTj/mv5tAs6xidCNnD9qVUFxA0w0lEcf+MyfhLa6hNXmnPf42QZ7BF3JVYgWirYB2RX0iYpGQlTDBTXcwiRqIYvaHG6ivZVg9PyzG/RG2JU6Dp0+KzvQCWtN/2wHnLfPOVuuYy9dI50yeKtrSvw/FiX+j/ohXxHwK9PbD0bSrY/gQytEkpsZ/tEjEeHwnDb07hvhmGY1bt+y0MIwJnqk18KBY5WkmnG1L/m9dZkslVjgQ8iHudbdJ7GF0jxxFxuPH/W/5hXN9YIiO8StTMDhxWkxLJN6r9QamNyrQGPx9df25cb4YCJODSfZ1dSKpuFkAtXuig0ZG8Pvte7q4FE3R4XA3Ys0GNMl+Kq40GpgqV0ljWz4oF174yvzS300OtmvQ7xM9brclwsFNz7rcuLNegLjQGaKAw4F9Hg+8soy15hbmNmto8cHzleJLvfS/YAwzzP0eLxKuDtR0HdObm1A1zY7pZ54AdXD1Lk7OJsszuI6Pa+or/W353BsgU7+HbW5yorZYxSebqvgXKMJ2hQtpEroAAAAASUVORK5CYII="class="icon"><span>Delete</span></button><button id="clear-selection"><img src="data:image/png;base64,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"class="icon"><span>Clear Selection</span></button></div><div id="breadcrumb-container"><div class="breadcrumb"id="breadcrumb"></div><div id="status-container"><div id="progressbar-container"><div id="progressbar"></div></div><div id="memory-status"></div></div></div><div class="file-list"id="file-list"ondrop="handleDrop(event)"ondragover="allowDrop(event)"><table id="file-table"><thead><tr><th>Select</th><th>Name</th><th>File Size</th></tr></thead><tbody><!--Dynamic file listing--></tbody></table></div><div id="error-message"style="color: red;"></div></div><div id="popup-overlay"class="popup-overlay"style="display: none;"><div id="popup-window"class="popup-window"><div id="popup-content"></div><button id="popup-close"class="popup-button">Close</button></div></div><script src="scripts.js"></script></body></html>'''.encode()

scripts = r'''document.addEventListener('DOMContentLoaded',function(){loadDirectoryContents('/');document.getElementById('upload').addEventListener('click',()=>document.getElementById('file-upload').click());document.getElementById('file-upload').addEventListener('change',handleFileInputChange);document.getElementById('download').addEventListener('click',downloadFiles);document.getElementById('move-to').addEventListener('click',moveTo);document.getElementById('copy-to').addEventListener('click',copyTo);document.getElementById('rename').addEventListener('click',renameFile);document.getElementById('new-folder').addEventListener('click',new_Folder);document.getElementById('delete').addEventListener('click',deleteFiles);document.getElementById('clear-selection').addEventListener('click',clearSelection);document.getElementById('popup-close').addEventListener('click',closePopup);updateStatus();setInterval(updateStatus,5000)});let currentPath='/';let selectedFiles=[];let popup_modal=false;let popupTimer;let upIconBase64="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAENklEQVR42p2WTWxUVRTH//fNR9vhTttpSwkfEogulI0L485oEBNTQxNXLmrUkLBS4mfjZ0JABGpAExokJSYS17oBwWAUhbgxGuPGFijETChlOm1npjN905n37nvv+L8zVRfaMOMkkztv3n3nd87/f86dUWjjpceXBSHgvpZWrT7T8kb98Yrs2GqwfUscF65EcN9qDdLSJn3UlcyAwaWRXiQEeP5yBb/9zEre77nr83fdoA+5kkx78s2ejLrHUVgyEeZDhZe/K+PmFCGHMup/A/SBZVHar53f09u1o8vBVDnElCvQCcCJKRy9VEH2moI7tjZkzRt6f1mky8fZvX14SDuYrIT4qUiPlSAIBN1JB/GY4NjFCuazhBzrVy0D9NtlqSc8fLkvg8e647jK4D8WI96hAVx8vmu+oKvDgRBy+mwJ5Vwc7okBdVeAfndJauLhzIsZDK9P4DpluVyIEIg04ptI4IXNdcUHutc5qAYhvriwhOpigpD1ak2AfqcsrqlhYl8fntmQwDQz/34xgm8E4gAhIYbB6wzuB7y2EK69nTGU+cX5r8owtRjc8Q3qXwD9RkmqXh2nXu/Ds5uSyC6HODsfYsUAHdS9vpq1BfirAFqBgJ1VZyW6S6FQDXDlXIkbKNfERvU3QB8uS9L3sP+FHoxsTqJKfacqEX5YCBAyUJzZe6zCBjZWJhvcfubqMoMYDQdBujuBIkv65RwrMZTrk0Gl9AdLIjGDoYeTGHpgHW7OGxQ8QQfbMMXIK+x7L5RGttFqFRbUuOa+/M07rMBBgFQjk9TGJFxKO32pjM5+DaUPlyQW+thEzYvM2mP2QSnCwH0JjO7S2NYJfH0rQMn6YD1gB5nQSsWgJFZuzCE77UXVZAdHIw6nnkCyLw7PDRCY2NpzkDlYkCPP6UabnrzhYYbwuGoaXWf6oePA0Jjq7TkUFjWyBze3Pgf2NfBRUUafSuGRPgenr3uYrQAxZQeN+pumwX6dLbtwC8uzA8iObWwP0D9WkJd2r8NOngKnrhssLFMb26qm2UmBKAR+iFohj5U/Upg5sbU9QO+RRdk7lMLj/TGcvOqhYCvAPx74HIyQAHOnCI+dOXv83vYAmQMLMmIr6HcwMUlAuSnRX7MQRgqGAP92nqtG/sM2K+h5b16eHk5hFyv4dNJHgRIp25p2DihTGNFknhn12TxUoLFwvF3AaF6eZAWPbojhs9/rKC9xszWZ7gZ2HuiBEGBycxBWUBrf3h4g/WpOntjNNt3i4MyvPkpLUfMwtcdDGEFYgW8lyuWRNGmUTm1rD6BfycnO4TQGU4JvJw0CTq1we2Sn2rap4lFtTZ7J0fw03HYBg2/mpP/BFGps/Br1dzi1hlMeBZz2aoiIwUOeXz4d1xxC9/P726xgJCu1QpGyqEb/C7Nm40NFQeNXjYcP7F8YewTpjgG4F/8b8CftPHDwwRULGgAAAABJRU5ErkJggg==";let folderIconBase64="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAADtElEQVR42r1V3WtcRRT/nbvZjd0k/UgqNqIPimiRqrVQQitIkRIp6IOiYBGf/B/6YouKVCzSJimxKSLWmFQJptJigvhJ6YOiD1raICmtSW2bdDfZbJrdfJo7c3rm4969KVZrig53mHvnzpzfOb/fmTOE/7jR/wJwbiexDhngpbBBmvDQJ3xbTtDAi8T1Tz2P+uad4MUFB6IZVFWF4rc9KJ48jg2fLR+EfnkWvL6lFyvubQTm8tY4WIv7hNnhIZx7cxc2nVg+lfTTDvCGd7uRvWcFeK5k3AdCDUqlMD38O357ey+a+m8D4Idm8KMHulHTWA1emLL2oRUoCFA6P4jTe/ajqubvFPzraaoCtvSB6Pvt4M0HulDbmJEIBMCIoA2KgFSvwXwxjXB2CmRkIHYOmJGlK23pZGPSfBvLZhTnpgZP40Lv+6BvtoGb2j5G3bq0AFxzANFmeag6Gxuy8wnD8ZxxiJVQ6/UTesuXLuLntvdAXz4J3traiZWNBmDSR8CWJrvYbFbRN1cMRyDaA+jEdwCURkbx4+Eu0PEt4G3tH2HVupRocM1vhDckMStV8dxSJ2Oo3Ki8Eyq0DrBfE0gGTl4examObtCxJvD29g+x0gBYDQyfsmF+QgCnAQuq3JylTblu5tL1QoeoGUgWZOpkXtaEi5LhhOKVEZzs+BTUsxncfOgIVq/V0JNnxKCALJQTOnh65J0tFRGQ6Yvyy0SwKH6lEWRWg2ruFrw7MXHpMr7rOAo6ugm8o20f1mQvQs8WHd/+LDheQ3kig95zG4V2xg2g+WdoE0BDVxBkMDm3Cl93nQJ1bgQ/0/IW6uuuQk8X4s2x15FBjkBdBFon6EqsN53EqYmxGXzVPwr64BHwc60CUDsCXR7zmXAzSpQ8CYM6Etj9Zx9RIAkwkZ9Df99V0OGHwS+0vYGGmisCkLPscJR2OinsDZQsEdw449aQ6XImCmPzONGXA7WvB7/U+joaav+ALuVtAHG4CQNLKFHJCFTFuAcyERTGF/B5Xx7U8iD4ldY9aMgOQ5XHK4fIR6BjsZXTgBOUJL9j6rRN03EB6PlCAPbfD3754G7clR2CKuXiYucoSYh4U0qUTwSf0tJSctDyBQE4JgDv3Ad+9dBurM0MyfkejfNf61vgOzTvob9DOK6uUoqQy/2Jzl7RYN8D4MeefgKPb7wDaqYgGyjOf1c2uFKTTOUMXemwnrOvUze0VIrw68AMzg6WHeZeiSIM/6HO/5srR9bKjYvXLsh9sNyb6lbbdQUO3sO94PfiAAAAAElFTkSuQmCC";let fileIconBase64="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAEQElEQVR42q2Wa2gcVRTH/3dmNpFo1LW1tQpVsPpBRYKCH3xBNVpFCD4o2BYrPip+KFWUSmuzSKXGVrRYFBGUNLVG66NBQY2SUgVtIKlpikhe3W7DZjfNJrvJZmdn532v585uYrYbog29szNzH7Pzu+f8zz13GOaUd9t+E4IzeD6HEAJgDArkje4MyJocKnVM2yYy2RxiSR2de19gWKCwcwFr77o1qIdCKgqGi5xVQN7yYNguJg0DU7oP03IQHTuLobMZ2CZbEFI2sOebo+LJe+uwclk4aAs6CgUHuuUjZ5rI6XmkDAcutftTaXSc6MOdN16PzqE4fn3rWXZeAN91YcIjgEozdmE5eVhkRYascjlHf2ISA/E41t99C9q6TuOveGpeSFlH06GjYsPqEsD3yQQOByosy4JpFKCbPrlLwPFdDCTS6IrGEFn/IHzHw57vOtE/Ml4BKWvsaj0inqq/rQRwIAVnigLLJ0tMFwXbg+OIwHm9sQR6h9N4e+N9SE7pGBweR3tvFD2x0TJIGeDNL46Ip++fAVjgXJWBBEGnSZFlkNie40MRPs6M5/Bjz+kAMJ3LI+8LxJNjaOuO4afjA+j7+GVWAYh83iGef+D2WQs4Lw7LEPVLECmwdJFBWnScHArGdV0gL5yg/uepUZxJjmPwk1cqAVubfxabH7ljVgNOYs48xEoQuUZytoDnOsVAsDhp5GIsa6CmRsOJ6Aj2/dCN4eatlYAtH34vXl17TwDwCOAQoKo0JkoPC9JkmqLJcVxwl7SREUagdNbCZZdWo+tUArsP/Y6Rz16rBGza2yoaNzxctADSFRzShhBdtDnPeb4Cm9swPBt2nsEVFgFMrLgijGODcfJEO0YPbqsErGtqEbufawgABs1OkAV0RTUljBD5yKc6p1RRJeseie6RBTb1ei4mcgWsWnEl/uiL45l9h5Fq3V4JaIh8Kj7Y/HgAyBgWVC6Cl2rkFpUpxXAinykqWUSC+HSa3IVHwk/oBm6+dhmO/T2Cx5oOYuLLHZWA1TuaRcuWRwPAZL4QOD6I+kBshhA5qppgjhQmBFwkgR4ja0mDnIkbrg7jZHQU9Y37kfmq8f8B5hbZVCmdqlIRjRXB9AsRdIIsXrnkYgrTBNY0HsDk14sBULuqSoNLM1YVjVyngVM6UVgxnSwJ16B7KIGHIgcwtRgAAgtUiiIC0BEiMaSXpAMdSidLay8A4N8cw0orEMGmZHIfV9VeguMEWHMhAHLWMoRZIL5MIz6uubx2YcBNL74v2ndunAWweQDyD5xE9SWCQlSlhaFpGkxKgsvDZEFJ5P8EpKZ1WqHFfuUciGlTIqTcxlSaP0WVRgtvqmCh7rrl6IkmUb99P7LfRioBS594Q/R89NLslrmYIveGuk3vIX14ZyWgtuF10d+ybdEvnymr1u2C9cs78wPk3RXSKeK8Xio/cxjlr5kyA/gHM7+cN0oReEMAAAAASUVORK5CYII=";function updateStatus(){fetch('/status').then(response=>response.json()).then(data=>{updateProgressBar(data.progress);updateMemoryStatus(data.memoryFree,data.memoryTotal)}).catch(error=>{console.error('Error fetching status:',error)})}function updateProgressBar(progress){const progressBar=document.getElementById('progressbar');progressBar.style.width=progress+'%';progressBar.style.backgroundColor=`hsl(${120-(120*progress)/100},75%,62%)`}function updateMemoryStatus(free,total){const memoryStatus=document.getElementById('memory-status');memoryStatus.textContent=`${free}MB/${total}MB`}function allowDrop(event){event.preventDefault()}function handleDrop(event){event.preventDefault();let items=event.dataTransfer.items;if(items.length>0){handleItems(items)}}function handleFileInputChange(event){let files=event.target.files;let fileArray=[];for(let i=0;i<files.length;i++){fileArray.push(files[i])}if(fileArray.length>0){processFilesAndDirs(fileArray,currentPath)}}function handleItems(items){let entryPromises=[];for(let i=0;i<items.length;i++){let item=items[i].webkitGetAsEntry();if(item){entryPromises.push(processEntry(item,currentPath))}}Promise.all(entryPromises).then(()=>{loadDirectoryContents(currentPath);showNotification("Upload completed successfully!")}).catch((error)=>{showError("Upload failed: "+error.message)})}function processFilesAndDirs(files,path){let directoryStructure={};for(let file of files){let relativePath=file.webkitRelativePath||file.name;let pathParts=relativePath.split('/');let currentLevel=directoryStructure;for(let i=0;i<pathParts.length;i++){if(i===pathParts.length-1){if(!currentLevel._files){currentLevel._files=[]}currentLevel._files.push(file)}else{if(!currentLevel[pathParts[i]]){currentLevel[pathParts[i]]={}}currentLevel=currentLevel[pathParts[i]]}}}processDirectoryStructure(directoryStructure,path).then(()=>{loadDirectoryContents(currentPath);showNotification("Upload completed successfully!")}).catch((error)=>{showError("Upload failed: "+error.message)})}function processDirectoryStructure(structure,path){let promises=[];for(let key in structure){if(key==='_files'){for(let file of structure._files){promises.push(uploadFileToServer(file,path+'/'+file.name))}}else{let newPath=path+'/'+key;promises.push(createDirectory(newPath).then(()=>{return processDirectoryStructure(structure[key],newPath)}))}}return Promise.all(promises)}function processEntry(entry,path){return new Promise((resolve,reject)=>{if(entry.isFile){entry.file(file=>{uploadFileToServer(file,path+'/'+file.name).then(resolve).catch(reject)})}else if(entry.isDirectory){let newPath=path+'/'+entry.name;createDirectory(newPath).then(()=>{let dirReader=entry.createReader();readAllDirectoryEntries(dirReader).then(entries=>{let subEntryPromises=entries.map(subEntry=>processEntry(subEntry,newPath));Promise.all(subEntryPromises).then(resolve).catch(reject)})}).catch(reject)}})}function readAllDirectoryEntries(dirReader){let entries=[];return new Promise((resolve,reject)=>{function readEntries(){dirReader.readEntries((results)=>{if(results.length){entries=entries.concat(results);readEntries()}else{resolve(entries)}},reject)}readEntries()})}function createDirectory(path){return fetch(`/newfolder?data=${JSON.stringify({foldername:path})}`,{method:'POST'}).then(response=>{if(response.ok){showNotification("Directory "+path+" created successfully!");return response.text()}else{showError("Directory "+path+" upload failed!");throw new Error('Failed to create directory');}})}function uploadFileToServer(file,path){return new Promise((resolve,reject)=>{showNotification(" Uploading "+file.name+" Please wait... ");const reader=new FileReader();reader.onload=function(event){const fileSize=event.target.result.byteLength;const hexData=hexEncode(event.target.result);const xhr=new XMLHttpRequest();xhr.open("POST",`/upload;${path};${fileSize}`,true);xhr.setRequestHeader("Content-Type","text/plain");xhr.onreadystatechange=function(){if(xhr.readyState===XMLHttpRequest.DONE){if(xhr.status===200){showNotification("File "+file.name+" uploaded successfully!");resolve()}else{showError("Upload "+file.name+" failed!");reject(new Error("Upload "+file.name+" failed"))}}};xhr.send(hexData)};reader.readAsArrayBuffer(file)})}function hexEncode(buffer){const byteArray=new Uint8Array(buffer);return Array.from(byteArray,byte=>('0'+(byte&0xFF).toString(16)).slice(-2)).join('')}function resetPopupTimer(){clearTimeout(popupTimer);popupTimer=setTimeout(closePopup,8000)}function showPopup(content){document.getElementById('popup-content').innerHTML=content;document.getElementById('popup-overlay').style.display='flex';resetPopupTimer()}function closePopup(){document.getElementById('popup-overlay').style.display='none';popup_modal=false;clearTimeout(popupTimer)}function showError(message){popup_modal=true;document.getElementById('popup-close').style.display='block';showPopup('<p style="color: red;">'+message+'</p>')}function showNotification(message){popup_modal=true;document.getElementById('popup-close').style.display='block';showPopup('<p style="color: green;">'+message+'</p>')}function showLoading(message){popup_modal=false;document.getElementById('popup-close').style.display='none';showPopup('<p style="color: black;">'+message+'</p>')}function downloadAll(urls){var link=document.createElement('a');link.setAttribute('download',null);link.style.display='none';document.body.appendChild(link);for(var i=0;i<urls.length;i++){link.setAttribute('href',urls[i]);link.click()}document.body.removeChild(link)}function loadDirectoryContents(path){currentPath=path;updateBreadcrumb();console.log("Updating file list");if(document.getElementById('popup-overlay').style.display=='none'){showLoading("  Loading...  ")}fetch('/contents?path='+currentPath).then(response=>response.json()).then(data=>{const fileTable=document.getElementById('file-table').querySelector('tbody');fileTable.innerHTML='';if(path!=='/'){const row=document.createElement('tr');const selectCell=document.createElement('td');const nameCell=document.createElement('td');nameCell.style.cursor='pointer';nameCell.addEventListener('click',()=>loadDirectoryContents(path.substring(0,path.lastIndexOf('/'))||'/'));nameCell.innerHTML=`<img src="${upIconBase64}"class="file-icon">..`;const sizeCell=document.createElement('td');sizeCell.textContent='';row.appendChild(selectCell);row.appendChild(nameCell);row.appendChild(sizeCell);fileTable.appendChild(row)}const directories=data.contents.filter(file=>file.isDirectory).sort((a,b)=>a.name.localeCompare(b.name));const files=data.contents.filter(file=>!file.isDirectory).sort((a,b)=>a.name.localeCompare(b.name));const sortedContents=directories.concat(files);sortedContents.forEach(file=>{const row=document.createElement('tr');const selectCell=document.createElement('td');const selectInput=document.createElement('input');selectInput.type='checkbox';selectInput.addEventListener('change',()=>{if(selectInput.checked){selectedFiles.push(file.path)}else{selectedFiles=selectedFiles.filter(f=>f!==file.path)}});selectCell.appendChild(selectInput);const nameCell=document.createElement('td');const iconSrc=file.isDirectory?folderIconBase64:fileIconBase64;const icon=document.createElement('img');icon.className='file-icon';icon.src=iconSrc;nameCell.appendChild(icon);nameCell.appendChild(document.createTextNode(file.name));if(file.isDirectory){nameCell.style.cursor='pointer';nameCell.addEventListener('click',()=>loadDirectoryContents(file.path))}const sizeCell=document.createElement('td');sizeCell.textContent=file.isDirectory?'-':`${file.size}`;row.appendChild(selectCell);row.appendChild(nameCell);row.appendChild(sizeCell);fileTable.appendChild(row)});if(popup_modal==false){closePopup()}}).catch(error=>{showError(error.message)})}function updateBreadcrumb(){const breadcrumb=document.getElementById('breadcrumb');breadcrumb.innerHTML='';const pathParts=currentPath.split('/').filter(part=>part);const link=document.createElement('a');link.href='javascript:loadDirectoryContents("/");';link.textContent="\u00A0\u00A0/\u00A0\u00A0\u00A0";breadcrumb.appendChild(link);let path='';pathParts.forEach((part,index)=>{path+=`/${part}`;const link=document.createElement('a');link.href='javascript:loadDirectoryContents("'+path+'");';link.textContent=part;breadcrumb.appendChild(link);if(index<pathParts.length-1){breadcrumb.appendChild(document.createTextNode(' / '))}})}function downloadFiles(){let files=[];selectedFiles.forEach(file=>{files.push(`/download?path=${file}`)});downloadAll(files);clearSelection()}function moveTo(){const destination=prompt('Enter destination path:\n\nExamples:\nPath from root: \u00A0\u00A0\u00A0\u00A0 /Folder\nRelative path: \u00A0\u00A0\u00A0\u00A0 folder1/folder2');if(destination){showLoading("  Moving files...  ");fetch(`/move?data=${JSON.stringify({src:selectedFiles,dest:destination})}`,{method:'POST'}).then(function(response){if(response.ok){showNotification("Files moved successfully!");return response.text()}throw new Error('Something went wrong.');}).then(function(text){loadDirectoryContents(currentPath);clearSelection();showNotification("Files moved successfully!")}).catch(function(error){showError('Server error: '+error)})}}function new_Folder(){const folder_name=prompt('Enter new folder name:');let new_path=currentPath+'/'+folder_name;new_path=new_path.replace(/\/\//g,'/');if(folder_name){fetch(`/newfolder?data=${JSON.stringify({foldername:new_path})}`,{method:'POST'}).then(function(response){if(response.ok){return response.text()}throw new Error('Something went wrong.');}).then(function(text){loadDirectoryContents(currentPath);clearSelection();showPopup('Directory created successfully!')}).catch(function(error){showError('Server error: '+error)})}}function copyTo(){const destination=prompt('Enter destination path:\n\nExamples:\nPath from root: \u00A0\u00A0\u00A0\u00A0 /Folder\nRelative path: \u00A0\u00A0\u00A0\u00A0 folder1/folder2');if(destination){showLoading("  Copying files...  ");fetch(`/copy?data=${JSON.stringify({src:selectedFiles,dest:destination})}`,{method:'POST'}).then(function(response){if(response.ok){showNotification("Files copied successfully!");return response.text()}throw new Error('Something went wrong.');}).then(function(text){loadDirectoryContents(currentPath);clearSelection();showNotification("Files copied successfully!")}).catch(function(error){showError('Server error: '+error)})}}function renameFile(){if(selectedFiles.length!==1){alert('Please select exactly one file to rename.');return}const newName=prompt('Enter new name:',selectedFiles[0].split('/').pop());let new_path=currentPath+'/'+newName;new_path=new_path.replace(/\/\//g,'/');if(newName){showLoading("  Renaming files...  ");fetch(`/rename?data=${JSON.stringify({old_name:selectedFiles[0],new_name:new_path})}`,{method:'POST'}).then(function(response){if(response.ok){return response.text()}throw new Error('Something went wrong.');}).then(function(text){loadDirectoryContents(currentPath);clearSelection();showPopup('File renamed successfully!')}).catch(function(error){showError('Server error: '+error)})}}function deleteFiles(){showLoading("  Deleting files...  ");fetch(`/delete?files=${JSON.stringify(selectedFiles)}`,{method:'DELETE'}).then(function(response){if(response.ok){return response.text()}throw new Error('Something went wrong.');}).then(function(text){loadDirectoryContents(currentPath);clearSelection();showPopup('Files deleted successfully!')}).catch(function(error){showError('Server error: '+error)})}function clearSelection(){selectedFiles=[];document.querySelectorAll('#file-table input[type="checkbox"]').forEach(checkbox=>checkbox.checked=false)}'''.encode()

styles = r'''body{font-family:Arial,sans-serif;background-color:#f5f5f5;margin:0;padding:0}.file-manager{max-width:1200px;margin:auto;margin-top:10px;border:1px solid #ddd;border-radius:10px;background-color:#fff;box-shadow:0 0 10px rgba(0,0,0,0.1);overflow:hidden}.toolbar{display:flex;gap:10px;padding:6px;background-color:#f0f0f0;color:white;position:relative;max-width:1200px;top:0;z-index:1000}.toolbar button{padding:10px 15px;border:none;border-radius:5px;background-color:#a0a0a0;color:white;cursor:pointer;font-size:16px}.toolbar button:hover{background-color:#808080}.toolbar button img.icon{width:16px;height:16px;margin-right:5px;vertical-align:middle}.breadcrumb{margin-top:0px;padding:10px;font-size:18px}.breadcrumb a{text-decoration:none;color:#007bff;margin-right:5px}.breadcrumb a:hover{text-decoration:underline}.file-list{margin:10px;border:1px solid #ddd;border-radius:5px;overflow:auto;max-height:calc(100vh - 140px)}#file-table{width:100%;border-collapse:collapse}#file-table tr{border-bottom:1px solid #ddd}#file-table tr:last-child{border-bottom:none}#file-table tr:hover{background-color:#ddd}#file-table th,#file-table td{padding:10px;text-align:left}#file-table th{background-color:#f0f0f0}.file-icon{width:20px;height:20px;margin-right:10px;vertical-align:middle}#error-message{margin-top:10px;color:red}@media (max-width:750px){.toolbar button{padding:15px}.toolbar button span{display:none}.toolbar button img.icon{margin-right:0}}.popup-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.2);display:flex;justify-content:center;align-items:center;z-index:2000}.popup-window{background:white;border-radius:10px;padding:20px;box-shadow:0 0 10px rgba(0,0,0,0.2);max-width:90%;max-height:90%;overflow-y:auto}.popup-button{margin-top:20px;padding:10px 20px;background-color:#a0a0a0;color:white;border:none;border-radius:5px;cursor:pointer}.popup-button:hover{background-color:#808080}#breadcrumb-container{display:flex;align-items:center;justify-content:space-between}#status-container{display:flex;align-items:center;margin-right:10px}#progressbar-container{width:100px;height:20px;background-color:#ddd;border-radius:5px;overflow:hidden;margin-right:10px}#progressbar{height:100%;width:0;background-color:red;border-radius:5px;transition:width 1s,background-color 1s}#memory-status{font-size:14px;color:#333}'''.encode()

init = r'''import gc
from micropython import alloc_emergency_exception_buf
from .utilities import connect_to_wifi
from .web_server import WebServer
from .web_handler import *


__version__ = '0.0.2'
module_folder = 'filemanager'

try:
	module_folder = __file__.rsplit('/', 1)[0]

	if module_folder == __file__:
		module_folder = ''
except NameError:
	pass


alloc_emergency_exception_buf(128)
gc.collect()

# Start WWW serveru
webserver = WebServer(web_folder=f'/{module_folder}/www', port=80)

#region Handlers for filemanager
@webserver.handle('/contents')
def _handle_contents(client, path, request):
	handle_contents(client, path, request)

@webserver.handle('/upload')
def _handle_upload(client, path, request):
	handle_upload(client, path, request)

@webserver.handle('/download')
def _handle_download(client, path, request):
	handle_download(client, path, request)

@webserver.handle('/delete')
def _handle_delete(client, path, request):
	handle_delete(client, path, request)

@webserver.handle('/rename')
def _handle_rename(client, path, request):
	handle_rename(client, path, request)

@webserver.handle('/newfolder')
def _handle_newfolder(client, path, request):
	handle_newfolder(client, path, request)

@webserver.handle('/move')
def _handle_move(client, path, request):
	handle_move(client, path, request)

@webserver.handle('/copy')
def _handle_copy(client, path, request):
	handle_copy(client, path, request)

@webserver.handle('/status')
def _handle_status(client, path, request):
	handle_status(client, path, request)
#endregion

if connect_to_wifi():
	webserver.start()
	gc.collect()
'''.encode()

web_handler = r'''import os
import json
import socket
import binascii
from .utilities import (
	is_directory,
	read_in_chunks,
	convert_file_size,
	file_path_exists,
)


FM_500 = "HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\n"
FM_200_JSON = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n"
FM_200_TEXT = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"

def urldecode(str: str):
	dic = {"%21":"!","%22":'"',"%23":"#","%24":"$","%26":"&","%27":"'","%28":"(","%29":")","%2A":"*","%2B":"+","%2C":",","%2F":"/","%3A":":","%3B":";","%3D":"=","%3F":"?","%40":"@","%5B":"[","%5D":"]","%7B":"{","%7D":"}"}
	for k,v in dic.items(): str=str.replace(k,v)
	return str

def parse_query_string(query_string: str):
	query = query_string.split('?')[1]
	params = query.split('&')
	param_dict = {}

	for param in params:
		key, value = param.split('=')
		param_dict[key] = value
	
	return param_dict

def list_directory_contents(base_path: str):
	contents = []

	try:
		for entry in os.listdir(base_path):
			if base_path == '/':
				entry_path = '/' + entry
			else:
				entry_path = base_path + '/' + entry
			
			#print(entry_path)
			
			if is_directory(entry_path):
				contents.append({
					'name': entry,
					'path': entry_path,
					'isDirectory': True
				})
			else:
				contents.append({
					'name': entry,
					'path': entry_path,
					'isDirectory': False,
					'size': convert_file_size(os.stat(entry_path)[6])
				})
	except OSError as e:
		print("OSError:", e)

	return contents

def delete_path(path: str):
	if not file_path_exists(path):
		print(f"Path {path} does not exist.")
		return

	stack = [path]

	while stack:
		current_path = stack.pop()

		if is_directory(current_path):
			try:
				entries = list(os.ilistdir(current_path))
				if not entries:
					# Directory is empty, we can delete it
					os.rmdir(current_path)
					#print(f"Deleted directory: {current_path}")
				else:
					# Add directory back to stack to try again later
					stack.append(current_path)
					# Add entries to stack
					for entry in entries:
						entry_path = current_path + '/' + entry[0]
						stack.append(entry_path)
			except Exception as e:
				print(f"Error accessing directory {current_path}: {e}")
		else:
			try:
				os.remove(current_path)
				#print(f"Deleted file: {current_path}")
			except Exception as e:
				print(f"Error deleting file {current_path}: {e}")

def handle_contents(client: socket.socket, path: str, request):
	try:
		query_params = path.split('?path=')[1] if '?path=' in path else '/'
		full_path = query_params
		
		contents = list_directory_contents(full_path)
		response = json.dumps({"contents": contents})
		client.send(FM_200_JSON)
		client.send(response)
	except Exception as e:
		print("Error:", e)
		client.send(FM_500)
		client.send("Internal Server Error")

def handle_upload(client: socket.socket, path: str, request):
	try:
		_, filepath, filesize = path.split(';')
		filesize = int(filesize) * 2
		data_read = 0

		#print("Upload: " + str(filepath) + "    size: "  + str(filesize))
		#print("0%")

		with open(filepath, 'wb') as file:
			data = request[request.find(b'\r\n\r\n') + 4:]

			if data:
				data_read = len(data)

				if data_read % 2 == 0:
					file.write(binascii.unhexlify(data))
				else:
					data = data + client.read(1)
					file.write(binascii.unhexlify(data))

				data_read = len(data)

			while data_read < filesize:
				try:
					chunk_size = min(1024, filesize - data_read)
					chunk = client.read(chunk_size)
					file.write(binascii.unhexlify(chunk))
					data_read = data_read + chunk_size
					percentage = (data_read / filesize) * 100
					#print(f"{percentage:.1f}%")

					if not chunk:
						break
				except OSError as e:
					if e.args[0] == 116:  # ETIMEDOUT
						break
					else:
						raise e

		#print("File Saved")
		client.send(FM_200_TEXT)
		client.send("Upload successful")
	except Exception as e:
		print("Error during file upload:", e)
		client.send(FM_500)
		client.send("Upload failed")

def handle_download(client: socket.socket, path: str, request):
	try:
		file_path = urldecode(path).split('?path=')[1]
		file_name = file_path.split('/')[-1]

		if file_path_exists(file_path):
			client.send(f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Disposition: attachment; filename=\"{file_name}\"\r\n\r\n")
			with open(file_path, 'rb') as f:
				for piece in read_in_chunks(f):
					client.write(piece)
		else:
			client.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n")
			client.send("File not found.")
	except OSError as e:
		print("OSError:", e)
		client.send(FM_500)
		client.send("Internal Server Error")

def handle_delete(client: socket.socket, path: str, request):
	try:
		files = json.loads(urldecode(path).split('?files=')[1])

		for file_path in files:
			delete_path(file_path) 

		client.send(FM_200_TEXT)
		client.send("Files deleted successfully.")
	except OSError as e:
		print("OSError:", e)
		client.send(FM_500)
		client.send("Internal Server Error")

def handle_rename(client: socket.socket, path: str, request):
	try:
		query_params = json.loads(urldecode(path).split('?data=')[1])
		old_name = query_params['old_name']
		new_name = query_params['new_name']
		os.rename(old_name, new_name)
		client.send(FM_200_TEXT)
		client.send("File renamed successfully.")
	except OSError as e:
		print("OSError:", e)
		client.send(FM_500)
		client.send("Internal Server Error")

def handle_newfolder(client: socket.socket, path: str, request):
	try:
		query_params = json.loads(urldecode(path).split('?data=')[1])
		folderpath = query_params['foldername']
		os.mkdir(folderpath)
		client.send(FM_200_TEXT)
		client.send("New folder created successfully.")
	except OSError as e:
		print("OSError:", e)
		client.send(FM_500)
		client.send("Internal Server Error")

def handle_copy(client: socket.socket, path: str, request):
	try:
		query_params = json.loads(urldecode(path).split('?data=')[1])
		src_files = query_params['src']
		dest_path = query_params['dest']
		stack = []

		for src in src_files:
			stack.append((src, dest_path))

		while stack:
			current_src, current_dest = stack.pop()
			if is_directory(current_src):
				new_dir_path = current_dest + '/' + current_src.split('/')[-1]
				os.mkdir(new_dir_path)

				for entry in os.listdir(current_src):
					stack.append((current_src + '/' + entry, new_dir_path))
			else:
				with open(current_src, 'rb') as f_src:
					with open(current_dest + '/' + current_src.split('/')[-1], 'wb') as f_dest:
						for piece in read_in_chunks(f_src):
							f_dest.write(piece)

		client.send(FM_200_TEXT)
		client.send("Files copied successfully.")
	except OSError as e:
		print("OSError:", e)
		client.send(FM_500)
		client.send("Internal Server Error")

def handle_move(client: socket.socket, path: str, request):
	try:
		query_params = json.loads(urldecode(path).split('?data=')[1])
		src_files = query_params['src']
		dest_path = query_params['dest']
		stack = []

		for src in src_files:
			stack.append((src, dest_path))

		# Přesun souborů a adresářů
		while stack:
			current_src, current_dest = stack.pop()
			if is_directory(current_src):
				new_dir_path = current_dest + '/' + current_src.split('/')[-1]

				if not file_path_exists(new_dir_path):
					os.mkdir(new_dir_path)

				for entry in os.listdir(current_src):
					stack.append((current_src + '/' + entry, new_dir_path))
			else:
				os.rename(current_src, current_dest + '/' + current_src.split('/')[-1])

		# Smazání prázdných původních adresářů
		for src in src_files:
			delete_path(src)

		client.send(FM_200_TEXT)
		client.send("Files moved successfully.")
	except OSError as e:
		print("OSError:", e)
		client.send(FM_500)
		client.send("Internal Server Error")

def delete_path(path):
	if not file_path_exists(path):
		#print(f"Path {path} does not exist.")
		return

	stack = [path]

	# Iterační průchod pro mazání souborů a podadresářů
	while stack:
		current_path = stack.pop()

		if is_directory(current_path):
			try:
				entries = list(os.ilistdir(current_path))
				if not entries:
					os.rmdir(current_path)
				else:
					stack.append(current_path)

					for entry in entries:
						entry_path = current_path + '/' + entry[0]
						stack.append(entry_path)
			except Exception as e:
				print(f"Error accessing directory {current_path}: {e}")
		else:
			try:
				os.remove(current_path)
			except Exception as e:
				print(f"Error deleting file {current_path}: {e}")

def handle_status(client: socket.socket, path: str, request):
	try:
		s = os.statvfs('//')
		flash_total = (s[0] * s[2]) / 1024 ** 2
		flash_used = flash_total - (s[0] * s[3]) / 1024 ** 2
		usage_percent = flash_used / flash_total * 100

		contents = ({
			'progress': '{0:.1f}'.format(usage_percent),
			'memoryFree': '{0:.1f}'.format(flash_used),
			'memoryTotal': '{0:.1f}'.format(flash_total)
		})

		response = json.dumps(contents)
		client.send(FM_200_JSON)
		client.send(response)
		#print(response)
	except Exception as e:
		print("Error:", e)
		client.send(FM_500)
		client.send("Internal Server Error")
'''.encode()

utilities = r'''import os
import network
from time import sleep_ms


def file_path_exists(path: str) -> bool:
	try:
		os.stat(path)
		return True
	except OSError:
		return False

def is_directory(path: str) -> bool:
	try:
		return os.stat(path)[0] & 0x4000 != 0
	except OSError:
		return False

def read_in_chunks(file_object, chunk_size: int = 1024):
	while True:
		data = file_object.read(chunk_size)

		if not data:
			break

		yield data

def convert_file_size(size: int) -> str:
	units = 'Bytes', 'KB', 'MB', 'GB', 'TB'
	unit = units[0]

	for i in range(1, len(units)):
		if size >= 1024:
			size /= 1024
			unit = units[i]
		else:
			break

	return f'{size:.2f} {unit}'

def connect_to_wifi() -> bool:
	sta = network.WLAN(network.STA_IF)
	sta.active(True)

	if sta.isconnected():
		return True

	wifi_list = sta.scan()

	print('Wifi List:')
	for index, wifi in enumerate(wifi_list, start=1):
		print(f'    [{index}] {wifi[0].decode()}')

	selected = None
	while True:
		try:
			selected = int(input('Choose a wifi to connect: '))
			assert isinstance(selected, int) and 0 < selected <= len(wifi_list)
			break
		except KeyboardInterrupt:
			return False
		except:
			pass

	ssid = wifi_list[selected - 1][0].decode()
	password = input(f'Input password for {ssid}: ')

	sta.connect(ssid, password)

	while (not sta.isconnected()):
		status = sta.status()

		if status in [network.STAT_IDLE, network.STAT_GOT_IP, network.STAT_NO_AP_FOUND, network.STAT_WRONG_PASSWORD]:
			break
		elif status == network.STAT_CONNECTING:
			pass

		sleep_ms(200)

	sleep_ms(1000)
	status = sta.status()

	if status == network.STAT_GOT_IP:
		print("Wifi connected, network config:", sta.ifconfig())
		return True
	else:
		print(f'Connect wifi failed with status code: {status}')
		return False
'''.encode()

web_server = r'''import network
import socket
import _thread
from .utilities import (
	file_path_exists,
	read_in_chunks,
)


class WebServer:
	MIMETYPES = {
		"txt"   : "text/plain",
		"htm"   : "text/html",
		"html"  : "text/html",
		"css"   : "text/css",
		"csv"   : "text/csv",
		"js"    : "application/javascript",
		"xml"   : "application/xml",
		"xhtml" : "application/xhtml+xml",
		"json"  : "application/json",
		"zip"   : "application/zip",
		"pdf"   : "application/pdf",
		"ts"    : "application/typescript",
		"ttf"   : "font/ttf",
		"jpg"   : "image/jpeg",
		"jpeg"  : "image/jpeg",
		"png"   : "image/png",
		"gif"   : "image/gif",
		"svg"   : "image/svg+xml",
		"ico"   : "image/x-icon",
		"cur"   : "application/octet-stream",
		"tar"   : "application/tar",
		"tar.gz": "application/tar+gzip",
		"gz"    : "application/gzip",
		"mp3"   : "audio/mpeg",
		"wav"   : "audio/wav",
		"ogg"   : "audio/ogg"
	}

	def __init__(self, web_folder: str = '/www', port: int = 80):
		self.__web_folder = web_folder
		self.__webserv_sock = None
		self.__url_handlers = {}
		self.__port = port

	def get_mime_type(self, filename: str):
		try:
			_, ext = filename.rsplit(".", 1)
			return self.MIMETYPES.get(ext, "application/octet-stream")
		except:
			return "application/octet-stream"

	def serve_file(self, client: socket.socket, path: str):
		try:
			if path.startswith("/*GET_FILE"):
				file_path = path.replace("/*GET_FILE", "")
			else:
				if path == "/":
					path = "/index.html"

				file_path = self.__web_folder + path

			mime_type = self.get_mime_type(file_path)
			filestatus = 0 # 0=Not found  1=Found  2=found in GZip

			if file_path_exists(file_path + '.gz'):
				filestatus = 2
				file_path += '.gz'
			elif file_path_exists(file_path):
				filestatus = 1

			if filestatus > 0:
				with open(file_path, 'rb') as file:
					client.write(b'HTTP/1.1 200 OK\r\n')
					client.write(b"Content-Type: " + mime_type.encode() + b"\r\n")

					if filestatus == 2:
						client.write(b'Content-Encoding: gzip\r\n')

					client.write(b'\r\n')

					for piece in read_in_chunks(file):
						client.write(piece)
			else:
				client.write(b"HTTP/1.0 404 Not Found\r\n\r\nFile not found.")
		except OSError as e:
			print("OSError:", e)
			client.write(b"HTTP/1.0 500 Internal Server Error\r\n\r\nInternal error.")
		except Exception as e:
			print("Exception:", e)
			client.write(b"HTTP/1.0 500 Internal Server Error\r\n\r\nInternal error.")

	def handle(self, pattern):
		"""Decorator to register a handler for a specific URL pattern."""
		def decorator(func):
			self.__url_handlers[pattern] = func
			return func

		return decorator

	def client_handler(self, client: socket.socket):
		try:
			request = client.recv(2048)

			if request:
				_, path, _ = request.decode("utf-8").split(" ", 2)

				for pattern, handler in self.__url_handlers.items():
					if path.startswith(pattern):
						try:
							handler(client, path, request)
						except Exception as e:
							print("Handler Exception:", e)
						client.close()

						return
				# Default file serving if no handler matches
				self.serve_file(client, path)
		except Exception as e:
			#print("Webserver Exception:", e)
			pass
		finally:
			client.close()

	def web_thread(self):
		while True:
			try:
				cl, _ = self.__webserv_sock.accept()
				cl.settimeout(2)  # time in seconds
				self.client_handler(cl)
			except Exception as e:
				#print("Webserver Exception:", e)
				pass

	def start(self):
		addr = socket.getaddrinfo('0.0.0.0', self.__port)[0][-1]
		self.__webserv_sock = socket.socket()
		self.__webserv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.__webserv_sock.bind(addr)
		self.__webserv_sock.listen(5)

		_thread.start_new_thread(self.web_thread, ())

		for interface in [network.AP_IF, network.STA_IF]:
			wlan = network.WLAN(interface)

			if not wlan.active():
				continue

			ifconfig = wlan.ifconfig()
			print(f"Web server running at {ifconfig[0]}:{self.__port}")

	def stop(self):
		if self.__webserv_sock:
			self.__webserv_sock.close()
'''.encode()

file_list = {
	'www/index.html': index,
	'www/scripts.js': scripts,
	'www/styles.css': styles,
	'__init__.py': init,
	'web_handler.py': web_handler,
	'utilities.py': utilities,
	'web_server.py': web_server
}


import os


module_folder = '/filemanager'

def install():
	def mkdir(path: str):
		try:
			os.mkdir(path)
		except OSError:
			pass

	def mkdirs(paths: list):
		cwd = module_folder

		for folder in paths:
			cwd += '/' + folder
			mkdir(cwd)

	mkdir(module_folder)

	for file, content in file_list.items():
		mkdirs(file.split('/')[:-1])

		with open(f'{module_folder}/{file}', 'wb') as output:
			output.write(content)

	import sys
	sys.modules.pop('filemanager')
	import filemanager

install()
