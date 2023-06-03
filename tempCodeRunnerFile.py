    for cell in cell_coords:
            numberText = text.render(str(coordinates.index(cell)), True, (0,0,0))
            screen.blit(numberText, cell_coords[cell_coords.index(cell)])