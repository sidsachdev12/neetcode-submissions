public class Solution {
    public double TimeTaken(int position, int speed, int target){
        return (double)(target - position) / speed;
    }

    public int CarFleet(int target, int[] position, int[] speed) {
        List<double> fleetStack = new();
        List<(int, int)> posWithSpeed = new();

        for (int i = 0; i < position.Count(); i++) {
            posWithSpeed.Add((position[i], speed[i]));
        }

        posWithSpeed.Sort();

        for (int i = posWithSpeed.Count() - 1; i >= 0; i--) {
            double currentTime = this.TimeTaken(posWithSpeed[i].Item1, posWithSpeed[i].Item2, target);
            if (fleetStack.Count() == 0){
                fleetStack.Add(currentTime);
            } else {
                if (currentTime <= fleetStack[^1]) {
                    continue;
                } else {
                    fleetStack.Add(currentTime);
                }
            }
        }

        return fleetStack.Count();
    }
}
