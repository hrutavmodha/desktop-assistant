export function H1({ children }) {
    return (
        <>
            <h1 className="text-3xl font-bold">
               {children}
            </h1>
        </>
    )
}
export function H2({ children }) {
    return (
        <>
            <h2 className="text-2xl font-semibold">
                {children}
            </h2>        
        </>
    )
}
export default function H3({ children }) {
    return (
        <>
            <h3 className="text-xl font-semibold">
                {children}
            </h3>
        </>
    )
}
