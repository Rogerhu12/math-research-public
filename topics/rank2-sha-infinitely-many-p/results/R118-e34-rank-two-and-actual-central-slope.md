# R118：E34 的初等秩二及实际普通中心斜率判据

日期：2026-11-12。**可信度：已证明。主课题未完成。**

## 结论

固定 $E_{34}:y^2=x^3-1156x$。
两同源下降给其秩恰二、有理挠群 $C_2^2$；明确独立点是
\[
 \left(\frac{289}4,\frac{4335}8\right),\qquad
 \left(\frac{21025}{144},\frac{2964815}{1728}\right).
\]
这补上 R112 的独立初等证书，不再以数据库的 rank 条目作为证明。

对每个 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$，
设 $J_{34,p}$ 为 R115 真实次数六十八截面在原曲线微分尺度下的
单位区间 principal Mellin 系列，则
\[
 J_{34,p}(0)=0,\qquad
 \boxed{\Sha(E_{34}/\mathbb Q)[p^\infty]\text{有限}
                  \iff J_{34,p}'(0)\ne0.}
\]

## 完整接口

- 二同源源曲线 $C:y^2=x^3+289x$ 的下降像为 $\{1,17\}$，
  对偶曲线下降像为 $\langle-1,2,17\rangle$。
  保留对偶核因子给 $[C:2C]=2\cdot8/2=8$；
  模 $3,5$ 点数及无有理四挠点给 $C_{\rm tors}=C_2$。
  点 $(68,578),(144,1740)$ 的独立性由同一平方类无限下降证明。
- 导子 $f=68$、ray class 度 $512$；根数 $+1$、所有目标普通 $p$
  非异常、辅助 Coleman 因子 $-56$ 为单位；CM 塔满足原文两处 Leopoldt 条件。
- R37 广义 Jacobian 与互易式适用于这两个实际点，给反圆分 MW 块非退化。
  Perrin–Riou 完整 Selmer 主项与 Agboola–Howard 已发表主猜想比较遂给
  $\operatorname{ord}F^-\ge2+\operatorname{corank}\Sha[p^\infty]$，
  以及有限性当且仅当 $[T^2]F^-\ne0$。
- R115 的实际平方常数 $\kappa_{34}=e_4(4624\cdot68)^4\ne0$ 给
  \[
   F^{\Theta,-}_{34,p}(T)=\kappa_{34}\,68\,\Omega_{34,p}
   (1+T)^{\log\langle68\rangle/\log(1+p)}J_{34,p}(T)^2.
  \]
  普通周期、有限角色、两个阶乘与非单位误差均按完整插值保留。

所以两行线性卷积中的**实际**双积分若对无穷多 $p$ 非零，
则固定两曲线之一满足主目标。该双积分非零性仍未证明。

完整证明和已核一手来源见
[证明笔记](../notes/2026-11-12-e34-rank-two-and-central-slope-criterion.md)；
有限代数运算见[准确脚本](../scripts/check-e34-rank-and-theta-multiplier.py)。
