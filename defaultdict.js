const defaultdict = (def, current) => {
    return new Proxy(current, {
        get: (target, key) => {
            if (!(key in target)) {
                target[key] = def();
            }
            return target[key];
        },
        set: (target, key, val) => {
            if (!(key in target)) {
                target[key] = def();
            }
            target[key] = val;
        }
    })
};
const current = {
    blue: 2
};
const counter = () => {
    if (!('added' in counter)) counter.added = 0;
    counter.added += 1;
    return 0;
};
const result = defaultdict(counter, current);
result.blue += 1;
result.red += 1;
result.green += 2;
console.log(result.red);
console.log('\n', counter.added)
