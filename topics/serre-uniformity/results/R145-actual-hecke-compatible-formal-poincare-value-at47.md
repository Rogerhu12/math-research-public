# R145：同一实际 Abel 框架中的 Hecke 相容 Poincaré 局部值

日期：2026-11-12。**状态：已证明；实际主函数、四个 126 次限制代数及整数范数全部独立验证通过。** 在 R141 的两组新 Abel 圆盘所定义的框架中，本文算得一个完整的非主局部 Poincaré 对数：
$$
\boxed{\Lambda^H\bigl(\sigma_{\rm new}(Y,Y)\bigr)
=4263370=47^2(3+41\cdot47)\pmod{47^4}.}
\tag{0.1}
$$
这里 $Y=mB_{-4}$ 是 R121 完整实际长乘所得的点，$m=\#J(\mathbf F_{47})$；纤维元素是下文明确指定的范数截面。此数是该局部纤维元素的值。它没有被标作全局自高度 $h(Y,Y)$，也没有被当成尚待构造的全局 QC 截面在某个 CM 点上的值。

## 1. 保持 R141 的同一规范框架

继续固定 $X=X_{\rm ns}^+(41)$、$\mathcal L=K_X+D$、$\deg\mathcal L=126$、$g=54$，在 $R_4=(\mathbf Z/47^4\mathbf Z)[i]$ 中计算。R141 的两组 54 个点记为 $Z_1,Z_2$，对应整逆 Abel 族为
$$
A_i(P)=Z_i(t_i(P))-Z_i.
\tag{1.1}
$$
它们所定义的双轴刚性化 Poincaré 范数框架为
$$
\mathcal P_{P,Q}=\operatorname{Norm}_{A_1(P)}\mathcal O(A_2(Q)),
\qquad \sigma_{\rm new}=1.
\tag{1.2}
$$
R141 已完整算出该框架的真实 $T_3$ 规范标量 Hessian $C$ 和整 Hecke 修正 $B$。

为在已有 Makdisi 模型内运算，按 R136 的实际算法选择
$$
D_i=\operatorname{div}(v_i)=Z_i+R_i,\qquad \deg R_i=72,
\quad E_i(P)=Z_i(t_i(P))+R_i.
\tag{1.3}
$$
于是 $E_i(P)-D_i=A_i(P)$ 逐除子成立。两个 $D_i$ 的实际不交性由 126 维限制映射的单位行列式验证；每个 $v_i$ 在 $Z_i$ 为简单零点，在其余 766 个原始评价点为单位。固定残余除子完全相消，所以本次使用的框架确实与 R141 相同。

## 2. 全部 820 个实际圆盘的三阶展开

源椭圆族仍为
$$
\mathscr E_t:y^2=x^3+x+32+t.
$$
从 R136 已固定的实际 41 阶挠点三阶展开出发，重新计算全部 1680 个权一 Eisenstein 截面的四个系数，再作 R102 的实际群平均和相对迹。得到所有 820 点、73 个权二截面的
$$
W(t)=W_0+tW_1+t^2W_2+t^3W_3+O(t^4).
\tag{2.1}
$$
程序检查：$W_0$ 是完整 R102 原矩阵，$W_1$ 是已发布的实际一阶矩阵；四个系数都满足 Frobenius 下降；在 R136 原来的 108 个点上，四个系数逐项等于原始已核三阶展开。

将式 (2.1) 限制到 R141 的新点组，乘 R123 校准的
$$
\beta(t)=-\frac3{4+27(32+t)^2}
$$
及实际典范嵌入矩阵。用整逆 Abel 算法求 $t_i(Y)$，得到真实的 73 维理想 $H^0(2\mathcal L-E_i(Y))$。两组代表分别移动离开固定 PicChart 除子后，与 R121 完整长乘终点的**全部 $820\times73$ 个 PicChart 值**逐项一致。故本次指数输入与实际全局点 $Y$ 的形式像一致。

源点 $Y$ 的整数乘数准确为
$$
m=21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072,
$$
其二进制长 304 位，$m\equiv9\pmod{47}$，R121 终点符号为正。对数直接读取已发布完整证书，而不重新选择基或周期。

## 3. 两个真实双逆主函数

用同一整逆 Abel 族求 $E_i(-Y)$。在 $V_2$ 中准确构造截面 $a_i$，使
$$
\phi_i=\frac{a_i}{v_i^2},\qquad
\operatorname{div}\phi_i=A_i(Y)+A_i(-Y).
\tag{3.1}
$$
这里复用 R138 的已证明实际算法：先用两个有效除子理想的乘积构成完整 199 维空间，再求秩 198 的主函数核，并验证所有 199 个乘积均被包含。因此式 (3.1) 包含真正的重数信息。按一个支集外的固定点令 $\phi_i=1$，还逐项核对
$$
\phi_i\equiv1\pmod{47^2}
$$
及完整 Frobenius 下降。

按 R138 的同一范数规范，两次逆运算作用在本框架上的实际标量为
$$
\delta_{\rm new}(Y,Y)
=\frac{\phi_1(Y)(A_2(Y))}{\phi_2(Y)(A_1(-Y))}.
\tag{3.2}
$$
第一变量逆运算给 $\phi_1(Y)(A_2(Y))^{-1}$；第二次逆运算再取倒数并乘相应第二范数，恰得到式 (3.2)。本文沿用该既有符号，不重新挑选对称框架。

## 4. 四个实际范数及其独立验证

用 R117/R138 的限制商和单生成代数算法，分别在 $E_2(Y)$、$D_2$、$E_1(-Y)$、$D_1$ 上构造实际 126 次有限平坦代数。每个代数都验证完整 $V_2,V_3$ 乘法及单位 Krylov 基。准确结果为：

| 有效除子 | 主函数 | 实际范数模 $47^4$ |
|---|---|---:|
| $E_2(Y)$ | $\phi_1$ | 3485803 |
| $D_2$ | $\phi_1$ | 2239927 |
| $E_1(-Y)$ | $\phi_2$ | 3691240 |
| $D_1$ | $\phi_2$ | 4521824 |

这里函数限制由真实截面商给出；有限代数中的分母为单位。独立验证器重新核对全部限制商、126 阶实际乘法算子和单位 Krylov 矩阵，并用整数结果式计算四个范数。遇到模 47 非单位的欧几里得首项时，验证器改用整数乘法矩阵行列式，未作非法除法。四个结果全部一致。

因此
$$
\begin{aligned}
\phi_1(Y)(A_2(Y))
&=3485803/2239927=1245877=1+12\cdot47^3,\\
\phi_2(Y)(A_1(-Y))
&=3691240/4521824=4049098=1+39\cdot47^3.
\end{aligned}
\tag{4.1}
$$
式 (3.2) 准确给出
$$
\boxed{\delta_{\rm new}=2076461=1+20\cdot47^3,\quad
\log\delta_{\rm new}=2076460,\quad
\tfrac12\log\delta_{\rm new}=1038230=10\cdot47^3.}
\tag{4.2}
$$

## 5. 接入完整 Hecke 相容局部对数

令 $z=\log(Y)$ 是 R121 的实际 54 维行对数；所有坐标都在 $47R_4$ 中。R141 的真实修正矩阵 $B$ 给
$$
\boxed{zBz^{\mathsf T}=3225140=47^2(3+31\cdot47).}
\tag{5.1}
$$
虚部准确为零，符合下降。R140 的完整 Hurwitz 分母界适用于此整框架及其真实 Lie 坐标：总次数 $n\ge4$ 的项在 $47\operatorname{Lie}(J)$ 上估值至少 $n-v_{47}(n!)\ge4$。因此它提供的是完整模 $47^4$ 局部值，而不只是丢掉未控制尾项的形式三阶表达。

对本框架中二次项为零的对数 $\Lambda_\sigma$，式 (4.2) 给出 $\Lambda_\sigma(\sigma_{\rm new}(Y,Y))$。再加真正的 Hecke 修正，得到
$$
\begin{aligned}
\Lambda^H(\sigma_{\rm new}(Y,Y))
&=\tfrac12\log\delta_{\rm new}+zBz^{\mathsf T}\\
&=1038230+3225140\\
&=4263370\pmod{47^4}.
\end{aligned}
\tag{5.2}
$$
这个值的 47 进估值恰为 2。此前的仅主除子范数和仅双逆三阶项现已通过 R141 真正规范 Hecke 同构接到一个明确的非主局部对数。

对任意纤维元素 $u\sigma_{\rm new}(P,Q)$，仍须加普通标量对数 $\log u$。若原始点不在形式群，需要用实际双扩张群律把该纤维搬入形式邻域，再利用群律的可加性除以搬运整数。全局 QC 截面的实际纤维比也必须计算；式 (5.2) 本身没有提供这些额外标量。

## 6. 稳定源码、紧凑证书和重做入口

新增源码：

- `scripts/p41_source_cubic47.gp`；
- `scripts/p41_source_cubic47.py`；
- `scripts/p41_hecke3_frame47.py`；
- `scripts/verify_p41_hecke3_formal_height47.py`。

复用已发布的 `p41_poincare_formal47.py` 以及独立的 `verify_p41_poincare_formal47.py` 中的主函数、限制代数检查。最终小型证书为

`scripts/data/p41_hecke3_formal_height47_compact.json.gz`，**15351 bytes**，SHA256

`2be64539b101b8f4363d14e813571e5853fb7b9163dbd21a171ab630674a3800`。

证书包含最终局部值、两组实际点编号及参数、基截面和主函数系数、四个单生成限制代数的多项式与范数，以及完整输入/源码哈希。四个新增源码的 SHA256 按上列顺序为：

```text
308e817024a200e77dff2c9e1ce039df0c5c0278b58b28c38b50e2fa6e32e01b
216ad4a60294c6123ac23716cfa96ce9af79da251b06883d1c767a5c9c99c8f7
2b29b2568234ff6bd8625569e2242a354ba27af76365760f6bd05a3a09fb93f4
74d8da78b6ec4e61a3d3a6aa07a75a02c0e7dcb24387a7669cd92a23f5fc0aab
```

可重建中间数据不入库，明确记录如下：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `p41_source_cubic47_checkpoint.json.gz` | 1863915 | `2eda1b699c8e556ab4d161868cb7152106520dd30a84008b2972e21e9a9312f4` |
| `p41_hecke3_abel_bases_checkpoint.json.gz` | 160316 | `2c0c16acee560af04582de86e345fe3ded57c8c0d5f8c5f56b2631aaf00e3a8d` |
| `p41_hecke3_exponential_checkpoint.json.gz` | 278841 | `574a3c584ff4b2dce97283ce52e62adcb102df9161c9ed2263726010f882c1f5` |
| `p41_hecke3_poincare_principal.json.gz` | 692720 | `b14baa59ef0ac8a8aee2e43e450f68851e02b64918cc6f3d2ad016b7a7a971ef` |
| `p41_hecke3_poincare_checkpoint.json.gz` | 4029314 | `83dfb53aeddab6533d2c2be3d6d0660abcab8646ae14fb4b6f2aadd2e30a69be` |

在课题目录运行；R136 和 R141 的完整原始中间文件若已清除，先按其重做入口恢复：

```bash
python scripts/p41_source_cubic47.py --script-dir scripts --gp /tmp/pari-2.19.0/gp
python scripts/p41_hecke3_frame47.py --script-dir scripts
python scripts/p41_poincare_formal47.py --script-dir scripts --bases /tmp/p41_hecke3_abel_bases_checkpoint.json.gz --jets /tmp/p41_source_cubic47_checkpoint.json.gz --exponential /tmp/p41_hecke3_exponential_checkpoint.json.gz --principal /tmp/p41_hecke3_poincare_principal.json.gz --output /tmp/p41_hecke3_poincare_checkpoint.json.gz
python scripts/verify_p41_hecke3_formal_height47.py --script-dir scripts --hessian scripts/data/p41_hecke3_hessian47_compact.json.gz
```

最终输出的五个核心整数应依次是
$$
2076461,\quad2076460,\quad1038230,\quad3225140,\quad4263370
$$
（依次为双逆单位、其对数、半对数、Hecke 修正和实际局部值）。完整结果和输入哈希还须与紧凑证书一致。

## 7. 证明依赖和后续接口

R136 提供真实整 Abel 指数和完整 PicChart 比较；R138 证明实际主函数、范数及双逆符号；R140 控制完整尾项并给规范 Hecke 相容化；R141 输出本框架的真正混合 Hessian。本文将这些接口在同一新框架中全部实际计算并独立验证。

下一步沿同一形式框架使用实际 AddFlip 主函数作 Miller 范数搬运，保持每一步纤维标量。R144 的 CM 差值校准可以消除处处非零全局截面的绝对常数，但仍须构造该全局截面或等价的规范纤维比。本文为这一计算提供了已知、完整且可恢复的局部终点值。
