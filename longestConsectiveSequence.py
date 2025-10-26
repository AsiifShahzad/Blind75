class Solution:
    def longestConsecutive(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        num_set = set(nums)
        longest = 0
        best_sequence = []

        for num in num_set:
            # Start of a new sequence
            if num - 1 not in num_set:
                current = num
                temp_sequence = [num]

                # Continue the sequence
                while current + 1 in num_set:
                    current += 1
                    temp_sequence.append(current)

                # Compare lengths and update if longer
                if len(temp_sequence) > longest:
                    longest = len(temp_sequence)
                    best_sequence = temp_sequence

        return best_sequence
