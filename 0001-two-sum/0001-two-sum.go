func twoSum(nums []int, target int) []int {
	m := make(map[int]int) // diff | index
	for index, value := range nums {
		diff := target - value
		if idx, found := m[diff]; found {
			return []int{idx, index}
		}
		m[value] = index
	}
	return nil
}
