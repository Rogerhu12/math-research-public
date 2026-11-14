# R288 附录：任意正权出生一 S1 的消逆式与次数九完整整数证书

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：已证明；精确证书已实际运行 PASS。** 对任意有限独立正权和旧上出生 $s=1$，本稿证明 [R275 首边加强充分式](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) (S1) 的严格版本。旧上高度为一时按真正硬顶取 $C_2=0$，也包括在内。结合[实际 S2 收缩附录](R288-appendix-birth-one-s2-contraction-and-weighted-coordinate-lift.md)，两条加强充分式均在出生一全部正权模型上支付。一般出生仍未由此闭合；已有出生一普通相邻定理不作为本稿新增结论重新计数。

计算只使用整数多项式与有限精确枚举，没有权值抽样或浮点符号判断。完整可重放文件为：

- [证书程序](../notes/2026-11-14-birth-one-s1-support-certificate-789f-next.py)；
- [本次实际运行结果](../notes/2026-11-14-birth-one-s1-support-certificate-789f-next.json)。

## 1. 完整物理算子及合法高度

取 $M\ge3$ 个正权，**本稿不先作单位归一**：
$$
d=\sum_{i=1}^M b_iE_i,\qquad b_i>0,\qquad z_i=b_i^2.
$$
记
$$
S=e_1(z),\quad Z=e_2(z),\quad W=e_3(z),\quad
T=\operatorname{diag}(z_i),\quad m_j=\sum_i z_i^j,
$$
$$
b=(b_i)_i,\quad K=b^\perp,\quad
P=I-\frac{bb^*}{S},\quad r=PTb,\quad t=PT^2b,\quad u=t-Sr.
\tag{1.1}
$$
下出生是真空，准确有 $L_2=Z^{-1}$、$L_3=W^{-1}$，三次桥 $B^*$ 在真空上的值为 $r$。

完整一孔 Gram 为
$$
F_1=dd^*|_{\mathcal H_1}=SI-2T+bb^*,
$$
$$
F_2=\frac{d^2(d^*)^2}{4}\bigg|_{\mathcal H_1}
=ZI-2ST+3T^2+Sbb^*-Tbb^*-bb^*T.
\tag{1.2}
$$
$F_1>0$ 对 $M\ge3$ 成立；$F_2>0$ 对 $M\ge4$ 成立。后一项可直接从三元子集和检验：若 $d^{*2}x=0$，则各三元集上的 $\sum x_i/b_i=0$；交换指标迫全部比值相同，再由一个三元和迫为零。当 $M=3$ 时 $F_2$ 秩一，其消去 $\mathbb Cb$ 的 Schur 补为零，正是 R275 规定的硬顶精度 $C_2=0$。

对 $M\ge4$，令 $C_j=(P F_j^{-1}|_K)^{-1}$；对 $M=3$ 保留相同 $C_1$ 并置 $C_2=0$。完整 $K\oplus\mathbb Cb$ Schur 补在两种情形都给
$$
\boxed{C_1=P(SI-2T)|_K-\frac{rr^*}{Z},}
$$
$$
\boxed{C_2=P(ZI-2ST+3T^2)|_K-\frac{uu^*}{W}.}
\tag{1.3}
$$
确切地，$F_1b=2(S-T)b$、$b^*F_1b=4Z$，而
$F_2b=3(Z-ST+T^2)b$、$b^*F_2b=9W$；对这些完整块消元便得 (1.3)。所有源仍是同一个 $K$。

创新与目标缺陷是
$$
\Delta=\frac12\left(\frac{C_1r}{W}-\frac rZ\right),
\qquad
\mathcal E=C_1^2-C_2-W\Delta\Delta^*.
\tag{1.4}
$$
本文证明 $\mathcal E\succ0$ 于 $K$，即严格 (S1)。

## 2. 真正创新的全部秩一项准确消去

Newton 的低阶恒等式，或直接展开，给
$$
m_2=S^2-2Z,\qquad m_3=S^3-3SZ+3W,
$$
$$
v:=\|r\|^2=m_3-\frac{m_2^2}{S}
=SZ+3W-\frac{4Z^2}{S}.
\tag{2.1}
$$
由 (1.3) 因而有
$$
C_1r=-2u-\frac{3W}{Z}r,
\qquad
\boxed{\Delta=-\frac uW-\frac{2r}{Z}.}
\tag{2.2}
$$
于是 $C_2+W\Delta\Delta^*$ 中的 $uu^*/W$ 抵消；剩余交叉再与 $C_1^2$ 中的交叉抵消。为明确保留压缩平方的代价，令 $H=P(SI-2T)|_K$，则
$$
H^2=P(SI-2T)^2|_K-\frac4Srr^*,
$$
$$
Hr=-2u+\left(S-\frac{4Z}{S}\right)r.
$$
代入 $C_1^2=(H-rr^*/Z)^2$，得到准确消逆身份
$$
\boxed{
\mathcal E
=P\operatorname{diag}\big((S-z_i)^2-Z\big)|_K
-\frac{SZ+W}{Z^2}\,rr^*.
}
\tag{2.3}
$$
没有把 $H^2$ 错换成未压缩平方，也没有先假设两个非交换项交换。

在 $S=1$、$p_i=z_i$ 的归一记号中，这正是
$$
P\operatorname{diag}\big((1-p_i)^2-e_2(p)\big)|_K
-\frac{e_2(p)+e_3(p)}{e_2(p)^2}\,rr^*.
$$
若写 $x_i=b_i y_i$，约束为 $\sum_i p_i y_i=0$，则待证标量二次型为
$$
\sum_i p_i\big((1-p_i)^2-e_2(p)\big)|y_i|^2
>\frac{e_2(p)+e_3(p)}{e_2(p)^2}
\left|\sum_i p_i^2y_i\right|^2
$$
对每个非零受约束向量成立。单个对角系数允许为负；后文没有逐坐标假定它们全正。

## 3. 去根号、去分母后的次数九矩阵

把 (2.3) 以 $P$ 延拓到完整 $\mathcal H_1$，使 $\mathcal E b=0$。令 $A_b=\operatorname{diag}(b_i)$，定义
$$
\boxed{\mathcal M_M(z)=S^2Z^2 A_b\mathcal E A_b.}
\tag{3.1}
$$
这是总次数九、整数系数、对称的矩阵多项式，且
$\mathcal M_M1=0$。没有在本式中对无界或非正权作逆变换。

置 $d_i=(S-z_i)^2-Z$。由
$$
\sum_i z_i d_i=3W
$$
展开 (3.1)，对 $i\ne j$ 得
$$
\boxed{
(\mathcal M_M)_{ij}
=z_iz_j\left\{
-SZ^2(d_i+d_j)+3Z^2W
-(SZ+W)(Sz_i-m_2)(Sz_j-m_2)
\right\}.
}
\tag{3.2}
$$
对角项准确为 $-\sum_{j\ne i}(\mathcal M_M)_{ij}$。

程序另从完整 $F_1,F_2$ 和创新重建矩阵，而不是只重算 (3.2)。具体令
$$
\widehat u_i=z_i(S-z_i),\quad
\widehat v_i=z_i(Z-Sz_i+z_i^2),
$$
$$
B_1=Z\,A_bC_1A_b,\qquad B_2=W\,A_bC_2A_b,
$$
其中 $C_1,C_2$ 按完整 Schur 补延拓为核含 $b$ 的算子。由 (1.2) 的矩阵显式展开可直接得到整数多项式 $B_1,B_2$。再置
$$
\tau_i=z_i(Sz_i-m_2),\qquad
q=S B_1(z_i)_i-W\tau.
$$
于是完整独立身份为
$$
\boxed{
4W\mathcal M_M
=4WS^2B_1\operatorname{diag}(z_i^{-1})B_1
-4S^2Z^2B_2-qq^*.
}
\tag{3.3}
$$
每个 $z_i^{-1}$ 均准确约去；程序逐次检查整除余数为零。对三位、四位实际完整矩阵，(3.3) 与 (3.2) 的所有条目已逐整数系数相等。该项检验亦包括硬顶三位的 $C_2=0$。

## 4. 有限支持为何穷尽任意位数

每个非对角项都有 $z_i z_j$ 因子；对角项由行和零给出。因此任一单项式 $z^\alpha$ 的系数矩阵仅作用于它的支持
$$
J=\{i:\alpha_i>0\}.
$$
把 $J$ 外变量置零，不改变该系数。由于 $S,Z,W,m_2$ 在零延拓下兼容，该系数与仅有 $|J|$ 个物理位时的同一公式完全相同，与环境 $M$ 无关。

令 $\mathcal M^{[J]}$ 收集恰好支持 $J$ 的全部单项式，则
$$
\boxed{
\mathcal M_M=\sum_{\substack{J\subset[M]\\|J|\le9}}\mathcal M^{[J]}.
}
\tag{4.1}
$$
支持一为空；支持二由 (3.2) 在两变量中恒等为零。程序完整检查了后一恒等。故只需支持 $m=3,4,\ldots,9$。

对这些 $m$ 定义
$$
K_m(z_1,\ldots,z_m)
=\frac{\mathcal M^{[\{1,\ldots,m\}]}}{z_1\cdots z_m}.
\tag{4.2}
$$
其总次数为 $9-m$，仍为对称整数矩阵多项式，且 $K_m1=0$。程序从 (3.2) 精确取出全部指数均至少一的单项式，再除去共同乘积；没有把可能坏的同支持单项式各自当作正矩阵。

## 5. 全部三十五个主子式的整数正系数证书

删去 $K_m$ 的最后一行、最后一列，得 $\widehat K_m$。对其阶数 $1,\ldots,m-1$ 的全部前导主子式，程序用列子集 Laplace 递推准确计算行列式。所有出现的整数系数均严格正，且每个行列式非零：

| 支持 $m$ | 矩阵次数 $9-m$ | 各阶前导主子式的非零系数数目 | 这些主子式中的最小系数 |
|---:|---:|---|---:|
| 3 | 6 | 17, 46 | 1 |
| 4 | 5 | 52, 276, 800 | 1 |
| 5 | 4 | 69, 493, 1817, 4840 | 5 |
| 6 | 3 | 56, 462, 2002, 6188, 15504 | 10 |
| 7 | 2 | 28, 210, 924, 3003, 8008, 18564 | 180 |
| 8 | 1 | 8, 36, 120, 330, 792, 1716, 3432 | 1890 |
| 9 | 0 | 1, 1, 1, 1, 1, 1, 1, 1 | 5040 |

完整 JSON 保留了每个主子式各自的最小系数、项数、非正系数计数，以及独立完整 Gram 恒等检验结果。上述总计 $2+3+4+5+6+7+8=35$ 个主子式。支持九时矩阵为常数；它同样经过完整行列式递推，没有仅凭模式猜测跳过。

当全部 $z_i>0$ 时，每个前导主子式严格正，Sylvester 判据给 $\widehat K_m>0$。结合 $K_m1=0$，有
$$
\boxed{K_m\succeq0,\qquad\ker K_m=\mathbb C1.}
\tag{5.1}
$$
这里最后一步是准确二次型身份：完整向量的值等于
$(x_1-x_m,\ldots,x_{m-1}-x_m)$ 在 $\widehat K_m$ 上的二次型。

程序使用 `python-flint` 的任意精度整数多变量多项式，不使用浮点运算。实际重放命令为
```bash
python topics/invariant-subspace-problem/notes/2026-11-14-birth-one-s1-support-certificate-789f-next.py --output topics/invariant-subspace-problem/notes/2026-11-14-birth-one-s1-support-certificate-789f-next.json
```
本次执行已完成并输出 `PASS`。支持计算合计约两秒；时间不参与数学证书。程序只有在支持九全部完成、所有主子式非零且全部系数严格正时，才给完整 `PASS`；任何负系数只表示该系数证书失败，程序没有把它冒称实际 Boolean 反例。

## 6. 拼回原实际创新预算与严格性

由 (4.1)、(4.2)、(5.1)，全部同支持组均半正定，所以 $\mathcal M_M\succeq0$。若一个全向量不是常数向量，选含两个不同坐标的三元子集；该三位支持组在这个向量上已经严格正，其他支持组均非负。因此对任意 $M\ge3$ 和正权，
$$
\ker\mathcal M_M=\mathbb C1.
$$
由 (3.1) 的可逆对角同余，$\ker\mathcal E=\mathbb Cb$，从而
$$
\boxed{
\Delta L_3^{-1}\Delta^*
\prec C_1^2-C_2\qquad\text{在同一个 }K_1=b^\perp\text{ 上}.
}
\tag{6.1}
$$
这条严格号不给跨所有权比的统一正余量。它支付的是实际三次桥创新所需的更强预算，不仅是旧 $C_2\prec C_1^2$。

与出生一 S2 的 $\|\mathcal T\|^2\le2/3$ 联合后，R275 两条无参数加强充分式在旧上出生一的全部独立正权模型上均成立。下出生真空的相邻块由标量 elementary-symmetric Newton 不等式支付，因而该范围中的完整 one-bit 首边 SOS 已有实际依据。这个范围仍不是一般出生，也不能替代整个课题 README 的完成标准。
