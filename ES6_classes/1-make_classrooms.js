/*eslint-disable*/
import ClassRoom from './0-classroom';

const initializeRooms = () => {
    const arr = [19, 20, 34];
    return arr.map((n) => new ClassRoom(n));
}
export default initializeRooms;