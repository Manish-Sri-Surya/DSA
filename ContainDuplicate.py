def ContainDuplicate(self,num:list[int])->bool:
        
        seen=set()
        for num in nums:

            if num in seen:
                
                return True
            seen.add(num)
        return False
                
