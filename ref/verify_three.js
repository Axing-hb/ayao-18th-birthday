// 验证 vendor/three.min.js 是不是可用的 UMD 构建（能在浏览器 <script> 下暴露全局 THREE）
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const file = path.join(__dirname, '..', 'assets', 'vendor', 'three.min.js');
const code = fs.readFileSync(file, 'utf8');

// 模拟浏览器环境：没有 module/exports/define，只有全局对象
const sandbox = {};
sandbox.window = sandbox;
sandbox.self = sandbox;
sandbox.globalThis = sandbox;
sandbox.console = console;

vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename: 'three.min.js' });

const THREE = sandbox.THREE;
if (!THREE) {
  console.error('FAIL: 没有暴露全局 THREE');
  process.exit(1);
}

console.log('OK: 全局 THREE 已暴露');
console.log('  REVISION     =', THREE.REVISION);
console.log('  有 Scene     =', typeof THREE.Scene === 'function');
console.log('  有 Camera    =', typeof THREE.PerspectiveCamera === 'function');
console.log('  有 Renderer  =', typeof THREE.WebGLRenderer === 'function');
console.log('  有 Geometry  =', typeof THREE.CylinderGeometry === 'function');
console.log('  有 Material  =', typeof THREE.MeshStandardMaterial === 'function');
console.log('  有 Light     =', typeof THREE.DirectionalLight === 'function');

// 实测能否构建 3D 场景对象（不需要 WebGL 上下文）
const scene = new THREE.Scene();
const cake = new THREE.Group();
cake.add(new THREE.Mesh(
  new THREE.CylinderGeometry(1.5, 1.5, 0.6, 48),
  new THREE.MeshStandardMaterial({ color: 0xfffdf7 })
));
scene.add(cake);

// 数一下蜡烛能不能加到 18 根
let n = 0;
for (const [count, r] of [[6, 0.45], [12, 0.85]]) {
  for (let i = 0; i < count; i++) {
    const a = (i / count) * Math.PI * 2;
    const c = new THREE.Mesh(
      new THREE.CylinderGeometry(0.045, 0.045, 0.5, 12),
      new THREE.MeshStandardMaterial({ color: 0xfffdf7 })
    );
    c.position.set(Math.cos(a) * r, 1.75, Math.sin(a) * r);
    cake.add(c);
    n++;
  }
}
console.log('  蜡烛数       =', n, n === 18 ? '(18 根 ✓)' : '(不是 18！)');
console.log('  scene 子节点 =', scene.children.length);
process.exit(n === 18 ? 0 : 1);
