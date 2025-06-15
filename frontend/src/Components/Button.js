export default function Button({ children, ...props }) {
    return (
        <>
            <button 
            className="align-center bg-blue-600 hover:bg-blue-700 h-[35px] text-white w-[240px]  px-4 py-1 rounded-[7px] shadow transition duration-200 block mx-auto "
            {...props}>
                {children}
            </button>
        </>
    )
}
