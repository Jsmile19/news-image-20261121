import { copyFile, mkdir } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const source = join(dirname(fileURLToPath(import.meta.url)), 'entry.png');
const outputDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
await mkdir(outputDir, { recursive: true });
await copyFile(source, join(outputDir, 'entry.png'));
console.log(`Wrote ${join(outputDir, 'entry.png')}`);
