export function H1({ children }) {
    return (
        <div>
            <h1 className="text-3xl font-bold">
               {children}
            </h1>
        </div>
    )
}
export function H2({ children }) {
    return (
        <div>
            <h2 className="text-2xl font-semibold">
                {children}
            </h2>        
        </div>
    )
}
export default function H3({ children }) {
    return (
        <div>
            <h3 className="text-xl font-semibold">
                {children}
            </h3>
        </div>
    )
}
