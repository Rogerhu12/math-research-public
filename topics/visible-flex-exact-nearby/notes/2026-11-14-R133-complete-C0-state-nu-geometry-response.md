# 完整状态/参数几何比较的实际原生记录

2026-11-14，visible-exact-astra-ac0d。**已完成的完整系数消费，结论是有明确状态半径与世界锚输入的比较定理。**

- 实际进程 session1498 正常退出0，耗时25.045895秒。
- strict3071 + 真根间隙1 + positive4650 =7722个完整闭盒；覆盖准确[0,25/8]、全角与真实mean。
- 状态半径上限1/1000，nu半径上限1/100000。实际非线性解及其误差半径未由本次计算供给。
- 原native完整保存每盒全部增益/mean与v间隙/紧支metric系数/从外向内累计积分；4,073,131 bytes gzip，未改写原始输出。
- native SHA256：`00efc0322a9aa82cd1f234899599ed3fbaff87edd35b8c9ac1331b229b276a55`。
- source SHA256：`3f5acd223d3d378c371cac24b38ce7e88644f9c7137f83619e3326bbe82810bd`。
- 源码、各输入完整字节SHA及实际process身份见同名前缀`-identities.json`。

严格向外上界为frame状态15.736315/nu .304809、position状态30.196406/nu .105999、frame anchor到position1.950540；代数曲率差状态141.332651/nu3.988052。原参考正特征值<3.856372；原参考绝对行和12.095499较粗，不能据此宣称12。证明采用已完整原residual native的实际绝对特征值11.092578014346，经本次误差费得到条件性11.233951与正部3.997745。

## 原输入与重建

三个输入分别是完整strict native（SHA23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a）、完整positive native（SHAea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d）和完整angular native（SHA7a3dd2c1d48b611f5d9a6bd8c2d7ebeeeb4c2f6a7c2bcc4f61f4d012be4e2f90）。它们已分别以原公开parts及重建身份保存；重组原bytes后核SHA，不能只拿摘要替代全行。额外曲率界来自已成7296原residual完整native6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1，无需重复运算。

准确原运行（从课题目录）：

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 -u scripts/fourfold_codazzi_complete_C0_geometry_response.py \
  --strict notes/2026-11-14-R133-final-strict-v2-ac1-complete-native.json.gz \
  --positive notes/2026-11-14-R133-current-positive-complete-ac1-native.json.gz \
  --angular /workspace/scratch/ac0d699811ad/geometry-verified-20261114/complete-angular-defect.json.gz \
  --out /workspace/scratch/ac0d699811ad/geometry-verified-20261114/complete-C0-state-nu-geometry-response.json.gz
```

输出存在时源程序拒绝覆盖。严格target primitive、原候选、全残差与几何ODE均未被本次重复求解。全部参数及源码身份均在原native，原候选与连续修复中心不混用。

本条完整证明见[状态与参数几何比较](../results/R133-supplement-complete-C0-state-and-nu-geometry-response.md)。仍须全global inverse/nu Schur/精确GC解、外帽世界锚、闭合与四marker；本条不授最终课题完成。
