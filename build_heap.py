# python3

def build_heap(data):
    def sift_down(root):
        nonlocal swaps
        min = root
        left = root *2 + 1
        right = root * 2 + 2

        if left < n and data[left] < data[min]:
            min = left

        if right < n and data[right] < data[min]:
            min = right

        if root != min:
            swaps.append((root, min))
            data[root], data[min] = data[min], data[root]
            sift_down(min)

    swaps = []
    n = len(data)
    for root in range(n // 2 - 1, -1, -1):
        sift_down(root)

    return swaps
    
def main():
    data = []
    input_type = input(" 'I' or 'F' :")
    if input_type == "I":
        n = int(input("Enter amount of elements: "))
        data = list(map(int, input("Enter the elements in a row: ").split()))
    elif input_type == "F":
        filename = input("File name: ")
        try:
            with open("tests/"+filename, 'r') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            return
        except ValueError:
            print("File format is invalid.")
            return

    if len(data) != n:
        print("Number of elements does not match.")
        return

    swaps = build_heap(data)
    print(len(swaps))
    for root, j in swaps:
        print(root, j)



if __name__ == "__main__":
    main()
