import { describe, it, expect} from "@jest/globals";

let port = 8000

describe("Ensure endpoints work", ()=>{
    it("Test hello world endpoint", async ()=>{
        let result = await fetch(`http://localhost:${port}/test`);
        let text = await result.text();
        expect(result).toBeDefined();
        expect(text).toBe("Hello")
        expect(result.status).toBe(200)
    })
})