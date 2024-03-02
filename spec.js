const os = require('os')

function getMachineSpecs() {
    const specs = {
        platform: os.platform(),
        arch: os.arch(),
        cpus: os.cpus(),
        totalMemory: os.totalmem(),
        freeMemory: os.freemem(),
        hostname: os.hostname(),
        networkInterface: os.networkInterfaces()

    };
    return specs;
}


function recommendUsage(specs) {
    const { totalMemory, cpus } = specs;

    const isGoodForGaming = cpus.length >= 4 && totalMemory >= 8 * 1024 * 1024 * 1024
    const isGoodForEditing = cpus.length >= 6 && totalMemory >= 16 * 1024 * 1024 * 1024

    const isGoodForMovies = totalMemory >= 4 * 1024 * 1024 * 1024

    const isGoodForOfficeWork = totalMemory >= 8 * 1024 * 1024 * 1024


    if (isGoodForGaming) {
        return 'The machine is recommended for gaming';
    } else if (isGoodForEditing) {
        return 'The machine is recommended for video editing';
    } else if (isGoodForMovies) {
        return 'The machine is recommended for movies';
    } else if (isGoodForOfficeWork) {
        return 'The machine is good for office work';
    } else {
        return 'The machine does not meet specific requirements for gaming, editing and office work'
    }


}


const machineSpecs = getMachineSpecs();
console.log(`Machine Specifications`, machineSpecs);

const recommendation = recommendUsage(machineSpecs);
console.log(`Recommendation`, recommendation);