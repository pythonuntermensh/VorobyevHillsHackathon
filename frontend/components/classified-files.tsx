import { convertEnglishToRussian } from "@/utils/formateFileType";

type ClassifiedFilesProps = {
  classifiedFiles: {[key: string]: string};
};

const ClassifiedFiles = ({classifiedFiles}: ClassifiedFilesProps) => {
  return (
    <div className="flex flex-col w-full">
      <p className="text-center text-lg font-semibold p-3">Результат классификации</p>
      {Object.entries(classifiedFiles).map(([fileName, fileType]) => (
      <div key={fileName} className="flex justify-between gap-x-6 py-3 my-1 border-y-2 border-dashed border-zinc-400">
        <p className="text-zinc-600 font-semibold max-w-[60%] md:max-w-[80%] line-clamp-2">{fileName}</p> 
        <p className="text-zinc-600 font-bold">{convertEnglishToRussian(fileType)}</p>
      </div>
    ))}
    </div>
  )
}

export default ClassifiedFiles;