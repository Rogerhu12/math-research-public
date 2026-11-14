# 任意四个独立正权的完整偶临界相位：最优常数一

日期：2026-11-14（UTC）。代理：literature_audit / 789f。

**状态：本文证明全部四个独立正权、整个三维 primitive 源上的相位费用不超过一。等权取等，不能将结论写成全部正权严格小于一。** 证明保留原物理内积、完整第一逆、真正第二顶逆和非交换次序；最后一个标量正性由完整整数系数证书给出。没有把有限取点当成一般证明。

## 1. 物理模型与定理

取任意 \(b_1,b_2,b_3,b_4>0\)，在正交子集基上定义
\[
d=\sum_{i=1}^4b_iE_i,
\qquad e=\sum_{i=1}^4b_i^{-1}E_i^*,
\qquad V=\ker d\cap H_1=b^\perp,
\qquad U=\ker d\cap H_2.
\]
\(V\) 是整个三维出生一源，\(U\) 是整个二维最高 primitive 源。记
\[
G=\Gamma_{1,1},\quad L=\Gamma_{2,1},\quad
A_0=e^*|_U:U\to V,\quad R_0=A_0A_0^*,
\]
\[
H_0=G^{-1}L-2G-R_0.
\tag{1.1}
\]
这里 \(\Gamma_{j,s}=\mathcal J_{j,s}^*\mathcal J_{j,s}\)，而 \(\mathcal J_{j,s}\) 是完整层 \(d^j/j!\) 的真正最小范数逆在 primitive 源上的限制。

**定理 1.1。** 对任意四个独立正权，
\[
\boxed{H_0^*L^{-1}H_0\preceq I_V.}
\tag{1.2}
\]
该常数一是最优的：四权相等时相位费用恰为 \(I_V\)。本文没有证明任意更大偶数位数的同一结论。

## 2. 三个实际物理矩阵的闭式

置
\[
z_i=b_i^2,\quad S=e_1(z),\quad q=e_2(z),\quad f=e_3(z),\quad
\pi=e_4(z)=\prod_i z_i,\quad p=\prod_i b_i=\sqrt\pi,
\]
并记 \(D=\operatorname{diag}(z_i)\)、\(P=P_V\)。

完整第一 Gram 在 \(H_1\) 上为
\[
F_1=dd^*=SI-2D+bb^*.
\tag{2.1}
\]
令 \(v=P b^3\)，其中 \(b^3=(b_i^3)_i\)。因
\[
PF_1b=-2v,\qquad b^*F_1b=4q,
\]
对 \(V\oplus\mathbb Cb\) 取完整 Schur 补，得到实际第一精度
\[
\boxed{C=G^{-1}=SI_V-2P D|_V-vv^*/q.}
\tag{2.2}
\]
这一步先保留整个 \(F_1\)，再完成 \(\mathbb Cb\) 的 Schur 消元；没有把 \(P F_1^{-1}P\) 换成 \((P F_1P)^{-1}\)。

第二归一删除 \(d^2/2:H_3\to H_1\) 是完整可逆矩阵。经补集将其输入识别为 \(H_1\)，矩阵为
\[
\frac{d^2}{2}\,\mathrm{comp}
=p\operatorname{diag}(b)^{-1}(\mathbf1\mathbf1^*-I)
\operatorname{diag}(b)^{-1}.
\]
所以它的完整逆是
\[
T_2=\left(\frac{d^2}{2}\,\mathrm{comp}\right)^{-1}
=p^{-1}(bb^*/3-D).
\tag{2.3}
\]
在 \(V\) 上 \(bb^*\) 消失，故
\[
\boxed{L=\pi^{-1}P D^2|_V.}
\tag{2.4}
\]
这里的 \(T_2\) 是完整二步逆，不能与另外的完整 \(\mathrm{comp}\,e\,d^\dagger\) 混用；后者在全 \(H_1\) 上的 \(bb^*\) 系数不同。本文只使用 (2.3) 在 \(V\) 上的作用，不引用其全层交换性或酉性。

令 \(c=(b_i^{-1})_i\)。实际完整对偶 Gram 是
\[
Q_{\rm all}=e^*e
=\left(\sum_i z_i^{-1}\right)I-2D^{-1}+cc^*,
\qquad Q_0=P Q_{\rm all}|_V.
\tag{2.5}
\]
由 \([d,e]=2I\) 在 \(H_1\) 上及真正 MP 正交分解，
\[
e|_V=2\mathcal J_{1,1}+A_0^*,
\quad \operatorname{Ran}\mathcal J_{1,1}\perp U,
\quad Q_0=4G+R_0.
\tag{2.6}
\]
因此同一个相位可写成
\[
H_0=CL+2C^{-1}-Q_0.
\tag{2.7}
\]

## 3. 保物理度量的三维坐标与消逆

使用 \(V\) 的固定非正交基
\[
E_i=b_i^{-1}e_i-b_4^{-1}e_4,\qquad i=1,2,3.
\]
其物理源度量与逆为
\[
H=\operatorname{diag}(z_1^{-1},z_2^{-1},z_3^{-1})
     +z_4^{-1}\mathbf1\mathbf1^*,
\]
\[
H^{-1}=\frac1S\mathcal H,
\qquad \mathcal H_{ij}=S z_i\delta_{ij}-z_i z_j.
\tag{3.1}
\]
以下 \(C,L,Q_0,H_0\) 的三维矩阵均为**算子坐标**，并非形式坐标。它们的物理伴随是 \(X^{*H}=H^{-1}X^*H\)。

由 (2.2)–(2.5) 直接得到整数多项式矩阵
\[
C=\mathcal C/q,\qquad L=\mathcal L/(S\pi),
\qquad Q_0=\mathcal Q/(S\pi),
\tag{3.2}
\]
其中对 \(1\le i,j\le3\)，
\[
\boxed{
\mathcal C_{ij}
=q(S-2z_i)\delta_{ij}+z_i(S-z_i)(z_j-z_4),
}
\tag{3.3}
\]
\[
\boxed{
\mathcal L_{ij}=S z_i^2\delta_{ij}-z_i(z_j^2-z_4^2),
}
\tag{3.4}
\]
\[
\boxed{
\mathcal Q_{ij}
=S(f-2\pi/z_i)\delta_{ij}
 +(S-2z_i)(\pi/z_j-\pi/z_4).
}
\tag{3.5}
\]
式中的 \(\pi/z_i\) 是其余三个变量的乘积，故确为整数多项式。比如由 (2.2) 计算 \(C\) 时，原来出现的 \(S^{-1}\) 项合并为
\(2q+\sum_i z_i^2=S^2\)，恰给出 (3.3)。

先不用任何采样，可消去 (2.7) 唯一剩余的逆。置
\[
W=CH_0=C^2L+2I-CQ_0.
\tag{3.6}
\]
由于 \(C>0\)，目标 (1.2) 准确等价于
\[
L-H_0H_0^*\succeq0
\quad\Longleftrightarrow\quad CLC-WW^*\succeq0.
\tag{3.7}
\]
第一个等价用矩形平方的非零谱相同，或对 \(L^{-1/2}H_0\) 直接用 \(X^*X\preceq I\iff XX^*\preceq I\)。第二个是同一个可逆 \(C\) 的同余；没有交换 \(C,L,Q_0\) 的次序。

转回欧氏形式并再作同一个 \(H^{-1}\) 同余，(3.7) 等价于对称矩阵
\[
CLC H^{-1}-W H^{-1}W^{\mathsf T}\succeq0.
\tag{3.8}
\]
这里出现普通转置，只因为物理 \(H\) 已完整消进同余。不能在 (3.6) 之前把 \(X^{*H}\) 当成 \(X^{\mathsf T}\)。

## 4. 完整整数多项式缺陷

定义
\[
\mathcal W=\mathcal C^2\mathcal L
             +2q^2S\pi I-q\mathcal C\mathcal Q.
\tag{4.1}
\]
它满足 \(W=\mathcal W/(q^2S\pi)\)。令
\[
\boxed{
\mathcal D=
\frac{q^2S\pi\,\mathcal C\mathcal L\mathcal C\mathcal H
      -\mathcal W\mathcal H\mathcal W^{\mathsf T}}
      {S^2\pi}.
}
\tag{4.2}
\]
对显式 (3.1)、(3.3)–(3.5) 做整数多项式运算，分子每个条目都被 \(S^2\pi\) 整除，商为对称、齐次次数十四的整数多项式矩阵。附属生成器对所有九个条目执行精确除法并断言余数为零，同时断言 \(\mathcal D=\mathcal D^{\mathsf T}\)。

把分母逐项代回，得到完整身份
\[
\boxed{
CLC H^{-1}-W H^{-1}W^{\mathsf T}
=\frac{\mathcal D}{q^4S\pi}.
}
\tag{4.3}
\]
因为 \(q^4S\pi>0\)，定理现在完全化为 \(\mathcal D\succeq0\)。

## 5. 前两个主子式的全排序锥证书

物理问题对位的置换酉协变。因此可将四个平方权按
\(0<z_1\le z_2\le z_3\le z_4\) 排序。置
\[
(z_1,z_2,z_3,z_4)=(x,x+y,x+y+z,x+y+z+w),
\quad x>0,\quad y,z,w\ge0.
\tag{5.1}
\]
在这个代换下，令 \(m_1=\mathcal D_{11}\)、
\(m_2=\mathcal D_{11}\mathcal D_{22}-\mathcal D_{12}^2\)。其完整展开满足：

| 多项式 | 齐次次数 | 非零整数系数个数 | 负系数个数 |
|---|---:|---:|---:|
| \(m_1\) | 14 | 416 | 0 |
| \(m_2\) | 28 | 3,094 | 0 |

每个列出的非零系数都是严格正整数。故 \(x,y,z,w>0\) 时两个主子式均严格正；含零间隙时至少非负。

## 6. 行列式的两个乘法锥证书

同一整数运算给精确分解
\[
\boxed{\det\mathcal D=\pi^2S^2q^8 F_{16}(z_1,z_2,z_3,z_4),}
\tag{6.1}
\]
其中 \(F_{16}\) 是齐次次数十六、含 393 项的整数多项式。生成器通过除以右端的正因子做精确除法，断言余数为零。完整 \(F_{16}\) 的所有系数存于证书文件，定义不依赖猜测分解。

\(F_{16}\) 在单纯加法锥下仍有负系数，所以不能把 §5 的证书误延伸到行列式。利用齐次性，先将最小权归一为一；所有排序四元组准确写成
\[
(1,u,uv,uv\omega),\qquad u,v,\omega\ge1.
\tag{6.2}
\]
按 \(u\ge\omega\) 或 \(u\le\omega\) 分为两个穷尽的区域：
\[
\begin{array}{c|ccc}
&u&v&\omega\\\hline
\text{区域 0}&1+a+b&1+c&1+a\\
\text{区域 1}&1+a&1+c&1+a+b
\end{array}
\qquad a,b,c\ge0.
\tag{6.3}
\]
这些代换是多项式代换，不引入有符号分母。对同一个 \(F_{16}\) 的全部展开，准确得到：

| 区域 | 展开总次数 | 非零整数系数个数 | 负系数个数 |
|---|---:|---:|---:|
| 0 | 37 | 3,849 | 0 |
| 1 | 37 | 2,465 | 0 |

每个非零系数均严格正。因此 \(a,b,c>0\) 时 \(F_{16}>0\)，而闭区域内 \(F_{16}\ge0\)。两区覆盖全部 (6.2)；不必另外假设互易权不变性。

现在取严格排序且相邻比满足 \(u\ne\omega\) 的权。这些权在全部正权中稠密，排序后在 §5 和 §6 相应区域的内部，所以 \(m_1,m_2,\det\mathcal D\) 全部严格正。Sylvester 判据给 \(\mathcal D>0\)。对其余正权，包括重复权和 \(u=\omega\)，由多项式连续性得到 \(\mathcal D\succeq0\)。由 (4.3)、(3.7) 得到定理 1.1。实对称正性也给相同复 Hilbert 源的 Hermitian 正性。

## 7. 完整证书、重建命令与独立规范核对

证明所需的所有多项式条目由 (3.1)、(3.3)–(3.5)、(4.1)–(4.2) 定义。配套文件是：

- [精确生成与核验程序](2026-11-14-four-bit-all-weight-even-phase-certificate-789f-next.py)。
- [完整系数证书](2026-11-14-four-bit-all-weight-even-phase-certificate-789f-next.json)：含 \(F_{16}\) 的全部 393 项、四个正系数展开的全部指数/整数系数及各自 SHA-256。

程序只使用整数多元多项式运算来证明 §4–§6。可从仓库根运行

```bash
python topics/invariant-subspace-problem/notes/2026-11-14-four-bit-all-weight-even-phase-certificate-789f-next.py --verify-original --output /tmp/four-bit-phase-certificate-789f.json
```

其中 `--verify-original` 另做一次独立的精确规范核对：在 \(b=(1,2,3,4)\) 上从完整子集包含矩阵求 \(F_1^{-1},F_2^{-1}\)、原二维最高核及倒数删除，再核对 (3.2) 的全部源矩阵和 (4.3) 的完整三维同余。该核对用有理算术，不参与任意正权的正性证明。一次完整重建及规范核对耗时约 0.493 秒，四个证书均零负系数。

## 8. 等权、锐性及适用边界

若四个权均为 \(b>0\)，则
\[
G=(2b^2)^{-1}I_V,\qquad L=b^{-4}I_V,
\qquad A_0=0,\qquad H_0=b^{-2}I_V,
\]
从而
\[
H_0^*L^{-1}H_0=I_V.
\]
生成器也准确断言 \(\mathcal D(1,1,1,1)=0\)。所以全正权结论必须是 \(\preceq I\)；不能由区域内部的严格系数证书推称所有正权严格收缩。

本文覆盖四个完全独立的正权及整个三维源，未限制为分组或单个表示型。它提供偶临界相位的一个非标量完整低维基例。虽然此前已证明“所有偶池的统一相位界足以推出所有加强高度”，单独的四位定理没有满足那个全称前提；任意更大偶数位数的统一有限相位预算、原 graph 接合及一般 Hilbert 不变子空间问题仍未完成。
