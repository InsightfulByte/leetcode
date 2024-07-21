class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        ans = []

        while i<m and j<n:
            if nums1[i]<nums2[j]:
                ans.append(nums1[i])
                i += 1

            else:
                ans.append(nums2[j])
                j += 1

        while i<m:
            ans.append(nums1[i])
            i+=1

        while j<n:
            ans.append(nums2[j])
            j+=1

        for k in range (len(ans)):
            nums1[k]=ans[k]
        