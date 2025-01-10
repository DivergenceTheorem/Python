print("----- Задание 1 -----")

my_list = [1, 2, 3, 3, 4, 4, 5, 6]
counts = {}

for i in my_list:
    counts[i] = counts.get(i, 0) + 1

duplicates = [x for x in counts if counts[x] > 1]
print(duplicates)
print(list(set(my_list)))

print("----- Задание 2 -----")

text = ("Is allowance instantly strangers applauded discourse so."
" Separate entrance welcomed sensible laughing why one moderate shy." 
" We seeing piqued garden he. As in merry at forth least ye stood." 
" And cold sons yet with. Delivered middleton therefore me at." 
" Attachment companions man way excellence how her pianoforte." 
" Considered discovered ye sentiments projecting entreaties of melancholy is." 
" In expression an solicitude principles in do. Hard do me sigh with west same lady." 
" Their saved linen downs tears son add music. Expression alteration entreaties mrs can terminated estimating."
" Her too add narrow having wished. To things so denied admire. Am wound worth water he linen at vexed.")

counts = {}

text = text.lower().replace(".", "").split()

for i in text:
    counts[i] = counts.get(i, 0) + 1

count = 0
for i in list(set(counts.values()))[::-1]:
    for j in counts.keys():
        if(counts[j] == i and count < 10):
            print(f"{j}: {i} occurences")
            count += 1
            
    
print("----- Задание 3 -----")

MAX_CAPACITY = 5000

equipment = {'Палатка':3000, 'Спальный мешок': 1500, 'Обувь': 300, 'Еда': 2000, 'Компас': 100, 'Аптечка': 500, 'Одежда': 2500, 'Деньги и документы': 200}
inventory = list(equipment.keys())
weights = sorted(list(equipment.values()))[::-1]

# Для решения этой проблемы, можно использовать backtracking algorithm
def find_combinations(nums, target):
    closest_sum = 0
    result = []

    def backtrack(current_combination, current_sum, start):
        nonlocal closest_sum

        if closest_sum <= current_sum <= target:
            if current_sum > closest_sum:
                closest_sum = current_sum
                result.clear()
            if current_sum == closest_sum:
                result.append(list(current_combination))

        for i in range(start, len(nums)):
            if current_sum + nums[i] <= target:
                current_combination.append(nums[i])
                backtrack(current_combination, current_sum + nums[i], i + 1)
                current_combination.pop()

    backtrack([], 0, 0)
    return result

weight_combos = (find_combinations(weights, MAX_CAPACITY))
equipment_combos = []
for i in weight_combos:
    temp_list = []
    for j in i:
        for x in inventory:
            if equipment[x] == j:
                temp_list.append(x)
    equipment_combos.append(temp_list)

print("ВСЕ ВОЗМОЖНЫЕ КОМБИНАЦИИ СНАРЯЖЕНИЯ, КОТОРЫЕ СУММАРНО ВЕСЯТ МАКСИМАЛЬНО БЛИЗКО К ГРУЗОПОДЪЕМНОСТИ РЮКЗАКА : ")
for i in equipment_combos:
    print(i)
                










