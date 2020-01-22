import csv
import numpy as np
import matplotlib.pyplot as plt

cat_1 = []
cat_2 = []

with open('dummy_data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ctr = 0
    for r in csv_reader:
        cat_1.append(r[1])
        cat_2.append(r[2])

cat_1 = cat_1[1:]
cat_2 = cat_2[1:]

# N = 500
x = str(cat_1)
y = str(cat_2)
# colors = (0,0,0)
# area = np.pi*3

# Plot
plt.scatter(x, y, s=area, c=colors)
#plt.title('Scatter plot pythonspot.com')
# plt.xlabel('x')
# plt.ylabel('y')
plt.show()


# print(cat_1)
# print(cat_2)



#     included_cols = [1]
#     included_cols2 = [2]

#     for row in csv_reader:
#         # content = list(row[i] for i in included_cols)

#         cat_1.append(row[i] for i in included_cols)
#         cat_2.append(row[i] for i in included_cols2)

#         # print(content)

# print(cat_1)








 #    line_count = 0
 #    for row in csv_reader:
 # #        if line_count == 0:
 # # #           print(f'Column names are {", ".join(row)}')
 # #            line_count += 1
 # #        else:
 #        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')

 #        line_count += 1
 #    print(f'Processed {line_count} lines.')

 # for line in csvfile.readlines():
 #        array = line.split(',')
 #        first_item = array[0]

 #    num_columns = len(array)
 #    csvfile.seek(0)

 #    reader = csv.reader(csvfile, delimiter=' ')
 #        included_cols = [1, 2, 6, 7]

 #    for row in reader:
 #            content = list(row[i] for i in included_cols)
 #            print content


# Create data
# N = 60
# g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
# g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N))
# g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N))

# data = (g1, g2, g3)
# colors = ("red", "green", "blue")
# groups = ("coffee", "tea", "water")

# # Create plot
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1, axisbg="none")

# for data, color, group in zip(data, colors, groups):
#     x, y = data
#     ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

#     plt.title('Matplot scatter plot')
#     plt.legend(loc=2)
#     plt.show()

# time = [0, 1, 2, 3]
# position = [0, 100, 200, 300]

# plt.plot(time, position)
# plt.xlabel('Time (hr)')
# plt.ylabel('Position (km)')

# Create data