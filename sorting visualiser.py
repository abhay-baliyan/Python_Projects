class SortingVisualizer:
    def print_arr(self, arr):
        print(" ".join(map(str, arr)))
    def get_arr(self):
        size = int(input("Enter number of elements: "))
        arr = []
        for i in range(size):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
        return arr
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    def bubble_sort(self, arr):
        count = 1
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    print(f"Step - {count}:\t", end="")
                    self.swap(arr, j, j + 1)
                    self.print_arr(arr)
                    count += 1
    def selection_sort(self, arr):
        count = 1
        n = len(arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                print(f"Step - {count}:\t", end="")
                self.swap(arr, i, min_idx)
                self.print_arr(arr)
                count += 1
    def insertion_sort(self, arr):
        count = 1
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(f"Step - {count}:\t", end="")
            self.print_arr(arr)
            count += 1
    def quick_sort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            print(f"After partition at index {p}:\t", end="")
            self.print_arr(arr)
            self.quick_sort(arr, low, p - 1)
            self.quick_sort(arr, p + 1, high)
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                self.swap(arr, i, j)
        self.swap(arr, i + 1, high)
        return i + 1
    def merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
            print(f"Merged [{left}-{right}]:\t", end="")
            self.print_arr(arr)
    def merge(self, arr, left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    def get_choice(self):
        print("\nChoose Sorting Algorithm:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Quick Sort")
        print("5. Merge Sort")
        return int(input("Enter choice: "))
def main():
    sv = SortingVisualizer()
    arr = sv.get_arr()
    choice = sv.get_choice()
    print("\nOriginal array:")
    sv.print_arr(arr)
    if choice == 1:
        print("\nBubble Sort:")
        sv.bubble_sort(arr)
    elif choice == 2:
        print("\nSelection Sort:")
        sv.selection_sort(arr)
    elif choice == 3:
        print("\nInsertion Sort:")
        sv.insertion_sort(arr)
    elif choice == 4:
        print("\nQuick Sort:")
        sv.quick_sort(arr, 0, len(arr) - 1)
    elif choice == 5:
        print("\nMerge Sort:")
        sv.merge_sort(arr, 0, len(arr) - 1)
    else:
        print("Invalid choice!")
        return
    print("\nFinal array:")
    sv.print_arr(arr)
if __name__ == "__main__":
    main()
