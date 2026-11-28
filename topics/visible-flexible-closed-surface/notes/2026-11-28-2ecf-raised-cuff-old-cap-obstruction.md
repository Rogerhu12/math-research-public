# 真实升高返回层后的旧整凸帽点对

[R292](../results/R292-raised-actual-core-versus-the-old-fixed-flat-cap.md) 给严格反例：R290 全底图加 216 双球控制及真实 `.08` 全带升高，虽然原核心内部有限近对明显改善，旧完整凸帽却产生新的法球障碍。这里使用同一旧凸帽的实际开平底，不使用可移动的标记代理。

先对真实原生前缀、全部释放 Hermite 格的端点与中点、完整平盘、下半反射和真法向作独立观察。共 82082 个实际点，26346554 个半径 `.194` 内近对，原核心最小法球比 `.0973108`（局部），远材料对 `.1066036`。这不是连续 reach 证明。真正旧帽平面到一实际核点的比仅 `.04581503`，所以随后取有理材料点 `s=259/256,u=pi/2`，用原全部 141 频、216 修正和准确阶跃证明 reach/D<47/2800。其整数检查自然结束 0。

以 `S` 为公开 scripts 绝对路径，`W` 为[18 张真实升领输入](2026-11-28-2ecf-eighteen-genuine-raised-cuffs-and-shortened-fixed-cap-throats.md)已经重生的目录：

```bash
python "$S/2ecf-released-raised-cuff-normal-ball-search.py" \
  --work "$W" --command-receipt "$W/polar-released-cut-true-flat40-full-exit.json" \
  --state "$W/polar-released-cut-flat40-enriched.json" \
  --field "$W/polar-released-cut-flat40-enriched.npz" \
  --correction "$W/polar-released40-actual-cartesian-hardspheres.json" \
  --height-shift .08 --output "$W/raised008-full-core-and-old-cap.json"
python "$S/2ecf-raised-cuff-exact-fixed-cap-obstruction.py" \
  --scripts "$S" --state "$W/polar-released-cut-flat40-enriched.json" \
  --field "$W/polar-released-cut-flat40-enriched.npz" \
  --correction "$W/polar-released40-actual-cartesian-hardspheres.json" \
  --output "$W/raised008-old-fixed-cap-exact-obstruction.json"
```

首条先把公开 scripts 的 Python 源码复制或链接到 `W`（原生产器逐同目录导入其已登记依赖）；配方中的 command receipt 只提供完整原输入文件名，其他对象逐 SHA 核对。实际 probe 的原报告在 scratch 的 `/tmp/visible-flex-2ecf-released-flat40-raised008-full-core-and-cap-normal-pairs.json`，精确报告在 `root-work/raised008-old-fixed-cap-exact-obstruction.json`。原报告不入 Git。

实际帽选错是本例特有障碍，不能推广成不存在定理；后继已经真正更换整个凸体和喉，见 R293。

## SHA-256

| 原件 | SHA-256 |
|---|---|
| `2ecf-released-raised-cuff-normal-ball-search.py` | `9931eafd0fbe5f4fd94fb09fcfb827cee71170dafa9cc7d396089a0ab2616625` |
| `2ecf-raised-cuff-exact-fixed-cap-obstruction.py` | `b1d802370d5632c17f0aba4a3053d7398808044cf76adcd45ff71871ebe480cf` |
| `raised008-old-fixed-cap-exact-obstruction.json` | `3ca256eba32d80a048e1ab220e4ba97c9049c6600be5fb2576c117d975b12ed9` |
| `visible-flex-2ecf-released-flat40-raised008-full-core-and-cap-normal-pairs.json` | `a5a60f44ef2b2e87b32dababc6ac571d46934f6a9132fa2f11494f8a43cbdcd8` |
