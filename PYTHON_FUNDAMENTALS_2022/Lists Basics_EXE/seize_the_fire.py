level_of_fire = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells_list = ["Cells: "]
for cells in level_of_fire:
    cell = cells.split(" = ")
    type_of_fire = cell[0]
    value_of_cell = int(cell[1])
    if type_of_fire == "High" and 81 <= value_of_cell <= 125 and water >= value_of_cell:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        cells_list.append("- " + str(value_of_cell))

    if type_of_fire == "Medium" and 51 <= value_of_cell <= 80 and water >= value_of_cell:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        cells_list.append("- " + str(value_of_cell))

    if type_of_fire == "Low" and 1 <= value_of_cell <= 50 and water >= value_of_cell:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        cells_list.append("- " + str(value_of_cell))
    else:
        continue
str_cells_list = "\n".join(str(x) for x in cells_list)

print(str_cells_list)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
