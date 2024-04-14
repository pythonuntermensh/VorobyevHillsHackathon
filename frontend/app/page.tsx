import { ArrowRight } from "lucide-react";
import Image from "next/image";
import Link from "next/link";

export default function Page() {
  return (
    <div className="flex flex-col justify-center items-center overflow-y-auto h-full p-2">
      <div className="flex flex-col text-center p-4 rounded-lg bg-white min-w-[100%] md:min-w-[50%] shadow-lg">
        <h1 className="animate-text bg-gradient-to-r from-teal-500 via-purple-500 to-orange-500 bg-clip-text text-transparent text-6xl font-black">Команда SHA-256</h1>
      </div>

      <p className="animate-typing overflow-hidden whitespace-nowrap text-white text-3xl mt-5 text-center">Кейс</p>
      <p className="text-white text-3xl underline text-center">Семантическая классификация документов</p>

      <Link 
        href="/upload-file" 
        className="flex items-center justify-center text-lg gap-x-3 text-white mt-6 button w-48 h-16 bg-blue-500 rounded-lg cursor-pointer select-none active:translate-y-2  active:[box-shadow:0_0px_0_0_#1b6ff8,0_0px_0_0_#1b70f841] active:border-b-[0px] transition-all duration-150 [box-shadow:0_10px_0_0_#1b6ff8,0_15px_0_0_#1b70f841] border-b-[1px] border-blue-400">
          <p>Начать</p>
          <ArrowRight />
      </Link>

        <div className="flex flex-col md:flex-row items-center justify-center gap-y-3 md:gap-x-3 my-10">
          <Image src="/1.png" width={100} height={35} alt="Россия - страна возможностей" />
          <Image src="/1.svg" width={100} height={35} alt="Цифровой прорыв" />
          <Image src="/2.svg" width={100} height={35} alt="Министерство экономического развития РФ" />
        </div>
    </div>
  );
}
