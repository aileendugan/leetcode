class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		my_dict = {}
		for index, x in enumerate(nums):
			if target - x in my_dict:
				return my_dict[target-x], index
			my_dict[x] = index	
