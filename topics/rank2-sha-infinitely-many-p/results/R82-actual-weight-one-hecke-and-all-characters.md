# R82：实际权一形式的完整角色与 Hecke 关系

日期：2026-11-12。状态：全文、原始规范及精确 cyclotomic 证书均已根端独审。
完整证明见[实际权一分解](../notes/2026-11-12-actual-weight-one-hecke-and-character-decomposition.md)，
证书见[整数环脚本](../scripts/check-weight-one-hecke-decomposition.py)。

## 1. 原256点的全部角色都保留

令 $N=68$，原导子轨道为
$\mathcal S=\langle-3,-2+i\rangle(1,-1)\subset(\mathbb Z/N)^2$，
$w=1_{\mathcal S}-1_{-\mathcal S}$，$\chi_4=\chi_{-4}$。
标量 $-3$ 生成全部模68且模4为1的单位，故准确有

$$
w(ua,ub)=\chi_4(u)w(a,b).
$$

对实际 R47 权一形式，置 $F(\tau)=\mathcal G(68\tau)/(2\pi i)$。
它在 $\Gamma_1(4624)$ 上，且完整 cusp 展开为

$$
F=4-\sum_{n\ge1}\sum_{de=n}C(d,e)q^n,
\qquad C(d,e)=\sum_{a\bmod68}w(a,e)\zeta_{68}^{ad}.
$$

按 $g=\gcd(d,68)$、$h=\gcd(e,68)$ 分层作有限乘法 Fourier 变换，
得到57个非零 Eisenstein 分量；其中模17的全部15个非平凡角色实际出现。
非本原角色的 Euler 因子和缩放层都保留。
唯一有非零常数的部分为 $16E_1(1,\chi_4)(1156\tau)$，其常数准确为4。
这不使用重叠导子情形下未适用的 cusp 常数定理。

## 2. 惰性处的全部同源迹

有限核的协变性直接给

$$
\langle p\rangle F=\chi_4(p)\sigma_{p^2}F,
\qquad T_pF=(1+\chi_4(p))\sigma_pF.
$$

因而对每个目标惰性 $p\ge7$，

$$
T_pF=0,\qquad U_pF=V_p\sigma_{p^2}F,
\qquad U_p^2F=\sigma_{p^2}F.
$$

令 $d_p=\operatorname{ord}_{17}(p^2)\mid8$，还得 $U_p^{2d_p}F=F$。
回到原 $\mathcal G$，关系是所有 $p+1$ 个同源分支的完整迹式；
它没有把一个 cusp $U_p^2$ 换成单个 Legendre crystalline Frobenius。

## 3. 准确作用于目标偶、奇截面

旋转轨道 $\mathcal S^{\rm rot}$ 满足相同协变。
取既定常数 $c_e=\sqrt2\,17^{17/4}/(4800f)$、
$c_o=i\sqrt2\,17^{7/4}/(32f)$，$f=34(1+i)$，置

$$
F_e=\frac{c_e}{2}(F-iF_{\rm rot}),\qquad
F_o=\frac{c_o}{2}(F+iF_{\rm rot}).
$$

实际除法单位模型给 $F_\bullet=\omega_1 M_\bullet/(2\pi i)$，
参数和周期均在 $68\tau$ 处取值。
惰性处 $X^4-17$ 的全部根在未分歧二次扩张中，$i,\sqrt2$ 也如此，
故 $\sigma_{p^2}$ 固定两个规范常数。上述三条 Hecke 关系分别对 $F_e,F_o$ 成立。

这是一条新的实际全局约束。除掉周期框架后，不能无修正地把 cusp $U_p$
用作 $M_e,M_o$ 或 $u=L/K$ 的系数抽取算子；已知奇部首项也不替代偶部中央行。
例如 $p=7$ 时 $T_7F=0$，而实际 $C_8/7\equiv2\pmod7$。

**剩余任务：** 在全部同源分支及真实微分运输中，将此约束接到完整中央导数，
证明其对无穷多个素数非零。精确脚本验证有限分解和规范，不把有限素数检查当作无穷性。
