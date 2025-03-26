export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const innertask = true;
    const innertask2 = false;
    console.log(innertask, innertask2);
  }

  return [task, task2];
}
