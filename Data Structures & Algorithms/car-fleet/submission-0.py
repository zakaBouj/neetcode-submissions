class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)

        arrivals = []
        for pos, spd in cars:
            arrivals.append((target - pos)/spd)

        stack = []
        for time in arrivals:
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)