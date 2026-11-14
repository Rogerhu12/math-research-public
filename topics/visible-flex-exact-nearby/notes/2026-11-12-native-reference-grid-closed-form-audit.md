# Native 有限参考网格：闭式复时间核查

2026-11-12，reproduce_newton。

源码 `scripts/fourfold_retarget_reference_native_grid.py` 的审阅/测试版本为
`8a11dc6da5417565ed00c8803a6b72bfa9382968e0b652b637fce3538366511a`。
本记录只覆盖有限参考算子的公式和一个已知闭式例；实际 δ₅ 第 419 段输入仍待
恢复后单独运行。它不能替代真实参考、场残差或流证明。

## 1. 源码口径

逐式检查了以下内容，未见实质问题：

- 负 Fourier 模先共轭各个时间多项式系数，再在同一个复时间 (u) 上评价。
  没有把非实 (u) 上的正模函数值直接共轭。
- 所有原始模的 (x) 导数先乘 (ik)，再按模数折叠到 DFT 网格。网格返回有限
  多项式的点值，不声称网格可以无混叠表示整个乘积。
- (Y=x/4+U+Qb)、(Y_u=U_u+Q_ub)、
  (Y_x=1/4+U_x+Q_xb+Qb_x) 的因子一致。前腿 (b=a)，后腿
  (b=Q_{f,\mathrm{end}}a)，后者导数保留完整乘积法则。
- `.bounds` 用实时间中心的实对称性支付
  (|\operatorname{Im}U_0(x+iS)|\le2\sum_{k>0}|U_{0,k}|\sinh(kS))，
  并对所有高阶复时间项使用完整有限 Wiener 模上界。
  静态乘积虚部用 (|\operatorname{Im}(ab)|\le|\operatorname{Im}a||b|
  +|a||\operatorname{Im}b|) 控制。
- `q_difference_from_real_time_center` 支付全部正时间阶，`full_Yu_modulus`
  包含准确时间阶因子。后者是归一化 (u) 的导数；转成物理 (tau) 导数仍须
  除以准确的段半长 (h)。源没有把这两个坐标混用。

## 2. 已实际执行的独立闭式例

定义准确有限函数

\[
 F(u,x)=1+2u+(1+iu)e^{ix}+(1-iu)e^{-ix}.
\]

在 (u=1/5+i/10)、
(x_l=2\pi l/N+i/128) 上，分别取 (N=1) 和 (N=8)。(N=1) 时正负非零模
全部折叠到同一 DFT 项，仍须给出准确点值。使用 192 bits，返回的 (F,F_u,F_x)
与独立闭式三式在全部九个点均相交；每个差的完整复球模上界小于 (10^{-50})。

精确重放命令（不需要任何实际参考分片）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python - <<'PY'
from fractions import Fraction
import sys
sys.path.insert(0,'scripts')
from flint import arb, acb, ctx
from fourfold_retarget_reference_native_grid import RealTimeFourier
ctx.prec=192
f=RealTimeFourier([[acb(1),acb(1)],[acb(2),acb(0,1)]])
u=acb(arb(1)/5,arb(1)/10)
for count in [1,8]:
    rows=f.grid(u,count,Fraction(1,128))
    for j in range(count):
        x=acb(2*arb.pi()*j/count,arb(1)/128)
        ep=(acb(0,1)*x).exp(); em=(acb(0,-1)*x).exp()
        want=[1+2*u+(1+acb(0,1)*u)*ep+(1-acb(0,1)*u)*em,
              2+acb(0,1)*ep-acb(0,1)*em,
              acb(0,1)*(1+acb(0,1)*u)*ep-acb(0,1)*(1-acb(0,1)*u)*em]
        for k in range(3):
            got=rows[k][j]
            assert got.real.overlaps(want[k].real)
            assert got.imag.overlaps(want[k].imag)
            assert abs(got-want[k])<arb('1e-50')
print('known complex-time conjugacy and derivative checks passed')
PY
```

这个例具体测试了复杂时间共轭约定、完整有限模 folding 以及归一化标签导数。
它不验证实际 (Y) 的非零导数、复像、与真实流的接近程度或整个标签连续域；
这些仍按各自冻结输入另行支付。
