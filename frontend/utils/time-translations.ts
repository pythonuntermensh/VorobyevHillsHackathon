export function floatToTime(time: number, isFlightDurationTime?: boolean) {
  const hours = Math.floor(time);
  const minutes = Math.round((time - hours) * 60);

  if (hours === 0 && isFlightDurationTime) {
    return `${String(minutes).padStart(2, '0')} мин.`;
  } else {
    return `${hours} ч. ${String(minutes).padStart(2, '0')} мин.`;
  }
}

export function convertTimeToFloat(timeString: string) {
  const [hours, minutes] = timeString.split(":").map(Number);
  return hours + minutes / 60;
}