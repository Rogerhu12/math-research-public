# R153 — 十六个完整类群源非分歧与无穷输入的源简单零

**状态：已证明。日期：2026-11-12。**

固定目标仍为 $E=389\mathrm a1$。将 R150 的 $D=-19$ 替换为
$D=-532$，其余十五域不变。新域的完整类群为 $C_2^2$，
实际 ramified 基是 $\{2,7\}$，并有 principal ordinary
$137=N(2+\sqrt{-133})$、$a_{137}(E)=-2$。
新十六域的平方类秩仍为 16。

对实际完整类群映射
$$
 \Phi_D=\sum_{d\mid D_0}\pi\circ d_d,\qquad
 f_D(\tau)=\sum_{d\mid D_0}d f(d\tau),
$$
以 $A=389D_0$、$b^2\equiv D\pmod{4A}$ 的真正 primitive CM
forms 给出全部层结构。每个域验证一个代表，由类群 Galois
作用和复共轭覆盖全部 $2h_D$ 个中心。
10000 项、两套独立整数 Fourier 系数和严格 Arb 尾界证明
十六个完整 $f_D(\tau_D)$ 全部非零；因此新族的全部 82 个
原 CM 中心均非分歧。$-19$ 的 512 位含零区间仅被记录为
未证，不被当成真零或非零结论。

令
$$
 g_{D,p}=\Theta^{p-2}\bar f_D/\mathrm{Ha}^p.
$$
它准确等于原 level 389 互反函数在全部 $d_d$ 点上的和。
Buium–Poonen 对原参数化的真实整数和给其在这些 CM 中心
取零，Igusa 导数为 $h-a_p(E)h^p$。

关键新规范是 CM 中心可能只定义在 $\mathbb F_{p^2}$ 上。
取 $\omega_{\rm Ig}=\Omega\omega_0$、
$\Omega^{p-1}=A=\mathrm{Ha}(\omega_0)$，则
$$
 h^{p^2}=A^{-2(p+1)}h,\qquad
 A^{p+1}\equiv\operatorname{Tr}\pi_{c,p^2}\pmod p.
$$
所以源导数为零迫
$a_p(E)^2\equiv(\operatorname{Tr}\pi_{c,p^2})^2\bmod p$。
实际 ramified 类代表 $\mathfrak a^2=(d)$ 给
$\pi_{c,p^2}=\pm\beta^2/d$、$N\beta=dp$。
固定二次型与 Hasse 界把全部源坏 p 计数为 $O(X^{3/4})$。

在 R149–R150 同一筛集合中，这些坏 p 至多造成
$O(x^{1-\theta/4})=o(x/\log x)$ 个坏 $\ell$，
$\theta=667/1000$。故存在一个固定新族域 $F_*$ 和无穷多个
实际 p，使 R150 的完整 Q 非扭、范数零、$\widehat h(Q)=o(p)$、
p 分裂且目标普通非异常等条件同时成立，并且实际源
$g_{D_*,p}$ 在所有原 CM 中心均为简单零点。

指定 $C_p$ 纤维的 $D_2Q$ 非零仍未证明；总 Hecke 迹简单零
不替代这个条件，主目标尚未完成。

[完整证明](../notes/2026-11-12-sixteen-unramified-cm-sources-and-square-frobenius.md)
给实际标签、全部区间、Hasse/周期方向、二次型计数和联合筛。
[可重复证书](../scripts/check-sixteen-full-class-cm-differentials.py)
只需已有 python-flint。
