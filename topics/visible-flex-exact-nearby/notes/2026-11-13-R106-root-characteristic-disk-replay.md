# R106：根整复盘特征商的待执行入口

2026-11-13，constructive-route。

**状态：新源已保存，尚未执行，不是数值证书。**

源文件为 scripts/fourfold_subprincipal_root_characteristic_disk.py。
它将在同一准确 $\delta_5\pm10^{-9}$ 家族、真正的 moving root 和无限 R33 原函数上，
直接包住整个 $|\rho|\le1/2500$、物理角带 $1/320$ 的特征商。

- 输入仍为 step5 exact-affine object 与实际 root-jet certificate。
- 不把已执行的根处 $|q|<1$ 或低阶 root jet 外推到复径向盘。
- 对真正有限 primitive 的全部保留径向系数，先付无限角误差和完整径向尾，
  再在每个闭角单元形成 $C=F_\theta\times F_r$、$G=C\cdot C$、
  $a_0=-C\cdot F_{\theta\theta}/G$、$b_0=C\cdot F_{r\theta}/G$。
- 曲率支由全盘实际 $K_{0,r}$ 的凸包支付：
  $-K_0(t-\rho)/\rho=\int_0^1K_{0,r}(t-z\rho)\,dz$。
- 只有每个闭角单元的完整复分母都通过，才输出
  $|q|=|b_0/a_0|$、$|k_*|=|\sqrt{-K_0/\rho}/a_0|$ 的共同上界。
  正根的 inward mixed 系数反号；此报告只给模长，反号不改变界。

此源复用冻结的真实几何函数；它不修改原函数。每 64 个完成角单元保存一个
checkpoint。根有限部、有符号相位、多项式近似误差及 R104 cutoff 均另付。

重放入口，在课题目录运行：

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python scripts/fourfold_subprincipal_root_characteristic_disk.py \
      --radial-radius 1/2500 --physical-strip 1/320 --angles 1024 \
      --out notes/2026-11-13-R106-root-characteristic-disk.json.gz

此次保存时 native 执行器 unavailable；不得据此创建一个伪造的通过报告。
上一轮真实 bulk/root-point/root-strip 执行的 receipt 与恢复入口仍在
notes/2026-11-13-R106-native-before-executor-loss-receipt.json 和
scripts/fourfold_subprincipal_recover_native_0102.py。
