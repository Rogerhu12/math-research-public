# 从已完成基础闭图延续非圆中央及全尾的实际求解

[R278](../results/R278-R262-true-convex-central-support-and-noncircular-width-continuation.md) 消费 R262 的全部真实中央系数、归一配速和原固定度量，从同一真实位置启动四个非圆态。Minkowski 目标椭圆半轴实算为 1.4487610929544836 和 .39876109295448364。真中央的未归一周长半径数值为 .9999999999999947，原中央物理周长由原定义准确等于 $2\pi$。物理前缀长与共同半核坐标总长分别约 2.021775895105453、2.4717758951054534，采用实际 cuff 半径的 $T_1$。

第一态 12 段位置样条、整数角至 9，直接在原保存场上全核更新。后续 24 段、整数角至 15，以准确 Boehm 公式给出嵌套基的数值转移，重新求中央和空间位置。第一态的两个观察组为 187×192 与 168×233；后续为 223×211 与 190×257。移位组同时沿径向和角向错开，包含中央、端口，尾半径从原精确物理查询集合选取，对原保存系数完整直接求值。原始 `parent/original` 观察始终是同一 `5778bee4…` 场。终图目标为原 $g$；初始中央输入和优化未知量与旧三重对称 shooting 不同，表里不同保存中央没有彼此冒充固定中央的纯空间加密。

再生采用 Bash、NumPy、SciPy。令 `S` 为公开课题脚本目录，`M` 为 [R262 再生记录](2026-11-28-2ecf-complete-original-G12-base-numerical-composition.md) 的原 M12 数据目录，`W` 为新输出目录。有理脚本读取原 .npz.gz；实际空间源直接读取原十二阶前缀、端点缓存、完整尾查询及原 W。运行时设置单线程 BLAS，以保证可复查的优化轨迹。

```bash
set -eu
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
mkdir -p "$W"
G="$M/h2-c2-m48-g12-04"
a=(--scripts "$S" --data "$M/m12-prefix-data.npz.gz" --grid "$G/grid.json"
   --query-report "$G/exact-tail-queries.json" --query-cache "$G/exact-tail-queries.json.npz"
   --field "$M/h2-c2-m48-g12-04r1/result.json.field.npz")
python "$S/2ecf-g12-actual-central-convexity.py" --data "$M/m12-prefix-data.npz.gz" --out "$W/g12-original-central-convexity.json"
python "$S/2ecf-r262-minkowski-physical-continuation.py" "${a[@]}" --eta .00390625 --output "$W/g12-mink-eta1over256.json"
python "$S/2ecf-r262-free-support-full-shape.py" "${a[@]}" --eta .00390625 --parent "$W/g12-mink-eta1over256.json" --spans 24 --modes 15 --support-max 12 --steps 8 --output "$W/g12-mink-free-eta1over256.json"
python "$S/2ecf-r262-fixed-width-free-support.py" "${a[@]}" --eta .00390625 --parent "$W/g12-mink-eta1over256.json" --spans 24 --modes 15 --support-max 12 --steps 10 --output "$W/g12-mink-width-eta1over256.json"
python "$S/2ecf-r262-free-support-full-shape.py" "${a[@]}" --eta .03125 --parent "$W/g12-mink-free-eta1over256.json" --spans 24 --modes 15 --support-max 12 --steps 9 --output "$W/g12-mink-free-eta1over32.json"
python "$S/2ecf-r262-minkowski-true-support-budgets.py" --data "$M/m12-prefix-data.npz.gz" --out "$W/g12-mink-support-four.json" "$W/g12-mink-eta1over256.json" "$W/g12-mink-free-eta1over256.json" "$W/g12-mink-width-eta1over256.json" "$W/g12-mink-free-eta1over32.json"
```

四个实际求解进程均完成。按 Fourier 系数绝对值分别累加曲率半径变化时，最后一个较大幅度态只得负的下界；改在全法向角的 64 个 Bernstein 闭区间上界定原有理多项式，得到正下界 .02704。这个证明保留相同求解场。

| 源码或产物 | SHA-256 |
|---|---|
| `2ecf-g12-actual-central-convexity.py` | `d27b8fdb211924801aa635a0c779a70c2ade9a49ff8f30e2d8e7d3098eeaa15e` |
| `2ecf-r262-minkowski-physical-continuation.py` | `87da8b2607d5cf22f7f71bbc3f63ccc21d4c0a2b10f47235b1300560f979f1b3` |
| `2ecf-r262-free-support-full-shape.py` | `333152774bc9db3ed1202c16b33bacf2cbf474f5e5fbe6d8498977bc0601ead5` |
| `2ecf-r262-fixed-width-free-support.py` | `1f0c118f1f277f0a2b68a77ed33726f53a1956bb729b386058290df084d1dd46` |
| `2ecf-r262-minkowski-true-support-budgets.py` | `f7897cdadf18cfe22c701ddd16f3efac0d5236019cf627fc8143a093d23dd63d` |
| `g12-original-central-convexity.json` | `6de4c884755d74e50886d074222c07b6f0b9ab150f9a1b8e5b26ad12ced428f7` |
| `g12-mink-eta1over256.json` | `106b4e755d08578b3a8580b6f6e3cb604d6369b5aeea0186986457828248a9a2` |
| `g12-mink-free-eta1over256.json` | `a7dda384e85fff08577e9c4cf18a22897679891e8c4c78f96ddbea4319046585` |
| `g12-mink-width-eta1over256.json` | `35e9a1413a2ec084109e4b68c37d6f5d9ba8de8a4347a3fffe8dd104a110103c` |
| `g12-mink-free-eta1over32.json` | `e13d263054b5383efeb0c974ee7555c662fe05211288ba7877431ab722bc2231` |
| `g12-mink-support-four.json` | `1f0cedea43d7df8468572f21e5d82ed86e20351f16a30f67c5e6c1d7719c1ceb` |
