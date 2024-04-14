"use client";

import ClassifiedFiles from "@/components/classified-files";
import FileUpload from "@/components/file-upload";
import { ArrowLeft, Link2 } from "lucide-react";
import Link from "next/link";
import { useState } from "react";

export default function Page() {
  const [isChoosingFiles, setIsChoosingFiles] = useState(true);
  const [classifiedFiles, setClassifiedFiles] = useState<{
    [key: string]: string;
  }>({});

  return (
    <div className="flex justify-center items-center overflow-y-auto h-full p-2">
      <div className="p-4 rounded-lg bg-zinc-100 min-w-[100%] md:min-w-[50%] shadow-lg">
        <div className="flex flex-col gap-y-3">
          <Link href={"/"} className="w-fit">
            <ArrowLeft className="w-8 h-8 rounded-full hover:bg-zinc-300 transition" />
          </Link>
          <Link
            href="/archive"
            className="flex items-center w-fit gap-x-1 text-sky-700 text-xl underline pb-3"
          >
            <div className="flex items-center gap-x-2">
              <p>В архив</p>
              <Link2 size={20} />
            </div>
          </Link>
        </div>
        {isChoosingFiles ? (
          <>
            <p className="text-sm font-semibold text-zinc-700 w-[80%]">
              Выберите файлы, которые необходимо классифицировать.
            </p>
            <FileUpload
              setIsChoosingFiles={setIsChoosingFiles}
              setClassifiedFiles={setClassifiedFiles}
            />
          </>
        ) : (
          <ClassifiedFiles classifiedFiles={classifiedFiles} />
        )}
      </div>
    </div>
  );
}
