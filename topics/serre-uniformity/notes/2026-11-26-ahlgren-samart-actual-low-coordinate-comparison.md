# Ahlgren–Samart 的实际系数与原低坐标的精确比较

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126。

本文核对外部非零定理究竟作用于哪个原坐标。它不重新证明或扫描已登记的低单位，也不把该单位替换成 O2 的高近 p 坐标。所有运算是下列有限恒等式的纸面推导；没有新增数学执行。

## 1. 命题及原归一

设 p=6a−1≥41 为素数，L=2a=(p+1)/3。采用
[R981](../results/R981-original-pure-Hurwitz-residue-compression.md)
的原模型
\[
E_+:y^2=x^3+1,\qquad \omega=dx/(2y),\qquad E_4=0,\ E_6=864,
\]
并令
\[
\beta=\mathscr B_p/12,\qquad \mathscr B_p=E_{p+1}(E_+,\omega).
\]
这里的 Eisenstein 归一、Robert 坐标与原题相同；没有引入另一个 Frobenius 基。

在 Ahlgren–Samart §4 的原 q=e^{2\pi i\tau} 下，准确取
\[
g=\eta(3\tau)^8,\qquad
w=\frac{\eta(\tau)^3}{\eta(9\tau)^3}+3,\qquad
G=gw^2=\sum_{n\ge-1}C_{\rm AS}(n)q^n.
\tag{AS.1}
\]
则在 \(\mathbf F_p\) 中
\[
\boxed{\quad C_{\rm AS}(p)=\frac92\beta^3.\quad}
\tag{AS.2}
\]
在本题原允许类内，结合已经证明的 R988(988.26)，准确地有
\[
\boxed{\quad
 C_{\rm AS}(p)\,\overline{\mathcal G_{3(p-1)}}=-\frac92.
\quad}
\tag{AS.3}
\]
所以这是固定低下标 3 的原纯 Hurwitz 坐标；它不是
\(\mathcal G_{(p-r)(p-1)}\)，也不是原 \(c_{p-r}^{\pm}\)。

## 2. 固定 modular 身份与尺度

令
\[
h=\frac{\eta(9\tau)^6}{\eta(3\tau)^2},\qquad
F=w^3-27,\qquad D=q\,d/dq.
\]
有
\[
g=h^2F,\qquad Dw=-hF.
\tag{AS.4}
\]
这里可直接核准每个身份。eta 商判据给
\(h\in M_2(\Gamma_0(9))\) 且特征平凡；它在无穷尖点的阶为 2，
在另三个尖点的阶为 0。\(w\) 仅在无穷尖点有一阶极点。
因此 \(h^2F\) 是全纯权 4 形式，展开至 Sturm 界 4 是
\(q-8q^4\)，与 \(g\) 相同。

同样，两边均为全纯权 2 形式的身份
\[
9E_2(9\tau)-E_2(\tau)=8h(w^2+3w+9)
\tag{AS.5}
\]
在 Sturm 界 2 内均为 \(8+24q+72q^2\)。
微分 \(w-3=\eta(\tau)^3/\eta(9\tau)^3\)，用 (AS.5) 得
\[
Dw=\frac{w-3}{8}\{E_2(\tau)-9E_2(9\tau)\}
=-h(w-3)(w^2+3w+9).
\]
这证明 (AS.4)，并固定微分的负号。

Guerzhoy–Kent–Ono 的 (1.12)、(3.5)、(3.6) 给
\[
f=w\sqrt h=a_{\rm cubic}(3\tau)
={}_2F_1\!\left(\frac13,\frac23;1;\frac{27}{w^3}\right)
=\sum_{i\ge0}A_iw^{-3i},\qquad
A_i=\frac{(3i)!}{(i!)^3}.
\tag{AS.6}
\]
其中 \(\sqrt h=\eta(9\tau)^3/\eta(3\tau)=c_{\rm cubic}(3\tau)/3\)。
首项为 q，因而平方根与相位均已指定，不存在任意单位比例。

## 3. Lucas 恒等式给实际 Cartier 多项式

置 \(d=L-1=(p-2)/3\)，
\[
A(T)=\sum_{i=0}^{d}A_iT^i,\qquad
S(w)=w^{p-1}A(w^{-3}).
\tag{AS.7}
\]
多项式 \(S\) 的最高、最低次数分别为 p−1、1，全部次数为 1 mod 3。

多项 multinomial Lucas 公式给
\[
A_{pm+j}\equiv A_m A_j\pmod p\quad(0\le j<p),
\]
且 \(3j\ge p\) 时 \(A_j\equiv0\)，因为三个低位相加有进位。
因此将 (AS.6) 作为 \(w^{-1}\) 的形式幂级数，
\[
f=A(w^{-3})\,f^p.
\]
由 \(f=w\sqrt h\)，得到
\[
h^{(p-1)/2}S=1,\qquad h^{1-p}=S^2.
\tag{AS.8}
\]

Ahlgren–Samart Proposition 4.2 的实际 Hecke 身份为
\[
G|T_4(p)=p^3G_p+C_{\rm AS}(p)g,
\]
其中 \(G_p\) 整。故
\[
G|U(p)\equiv C_{\rm AS}(p)g\pmod p.
\tag{AS.9}
\]
这里只用这一身份，没有把其 \(C_{\rm AS}(p)\) 单位定理当输入。

现在对同一个形式微分
\[
\nu=Gh^{-p}\frac{dq}{q}
=-w^2h^{1-p}\,dw=-w^2S(w)^2\,dw
\tag{AS.10}
\]
用 Cartier 算子。由 (AS.9) 和 (AS.4)，
\[
\mathcal C(\nu)=h^{-1}(G|U(p))\frac{dq}{q}
=-C_{\rm AS}(p)\,dw.
\tag{AS.11}
\]
另一方面，\(w^2S^2\) 的次数为 2p，全部幂次为 1 mod 3。
其可能贡献 Cartier 的次数为 p−1、2p−1；
后者为 0 mod 3，系数为零。因为 w 是 q 的可分局部参数，
这正是同一个 Cartier 运算，给出
\[
\boxed{\quad
C_{\rm AS}(p)=[w^{p-3}]S(w)^2
=\sum_{\substack{i+j=L\\1\le i,j\le L-1}}A_iA_j.
\quad}
\tag{AS.12}
\]
全部符号、首项与 q 尺度已在 (AS.1)、(AS.4) 保留。

## 4. 有限求和与 Wilson 因子

对 \(1\le i\le L-1\)，Wilson 给
\[
A_iA_{L-i}
=-\frac{(-1)^i(3i)(3i-1)}{(L!)^3}\binom Li^3
\pmod p.
\tag{AS.13}
\]
具体地，\(3(L-i)=p+1-3i\)，而
\((3i-2)!(p+1-3i)!\equiv(-1)^{3i-1}\)；
再乘 \((3i)(3i-1)\) 即得该负号。

设
\[
t_i=(-1)^i\binom Li^3,\qquad T_k=\sum_{i=0}^{L}i^k t_i.
\]
L 为偶数，故 \(t_{L-i}=t_i\)，从而 \(T_1=LT_0/2\)。
再将
\((i+1)^3t_{i+1}=-(L-i)^3t_i\)
从 0 到 L 求和，得到
\[
3LT_2-3L^2T_1+L^3T_0=0,\qquad T_2=L^2T_0/6.
\]
(AS.13) 可补入 i=0,L：首端的 \(3i\) 为零，
末端的 \(3i-1=3L-1=p\) 为零。于是
\[
C_{\rm AS}(p)
=-\frac{9T_2-3T_1}{(L!)^3}
=-\frac{3L(L-1)}{2(L!)^3}T_0
=\frac{T_0}{3(L!)^3}\pmod p.
\tag{AS.14}
\]

经典终止 Dixon 恒等式（DLMF 16.4.5 的有限特化）是
\[
T_0=\sum_{i=0}^{2a}(-1)^i\binom{2a}{i}^3
=(-1)^a\frac{(3a)!}{(a!)^3}.
\]
故
\[
\boxed{\quad
C_{\rm AS}(p)=
\frac{(-1)^a(3a)!}{3(a!)^3((2a)!)^3}\pmod p.
\quad}
\tag{AS.15}
\]
这里所有阶乘下标均小于 p。该公式也与已发表的低单位结论一致，
但不作为一条新的有限扫描结论登记。

## 5. 返回原 Robert 归一

[R973 方法](R973-original-balanced-Kronecker-four-prime-execution-method.md)
(973M.10) 指定
\[
B_{\rm old}
=(-1)^{(p-1)/2-(p-2)/3}
 \binom{(p-1)/2}{(p-2)/3}
=(-1)^a\binom{3a-1}{a}.
\]
R981(981.32) 的原模型转换是
\[
\mathscr B_p=12(-1)^aB_{\rm old},\qquad
\beta=\binom{3a-1}{a}
=\frac23\frac{(3a)!}{a!(2a)!}.
\tag{AS.16}
\]
Wilson 又给
\[
((3a-1)!)^2=(-1)^a,\qquad
((3a)!)^2=\frac{(-1)^a}{4}\pmod p.
\]
把 (AS.16) 代入 (AS.15)，准确得到
\[
\frac{C_{\rm AS}(p)}{\beta^3}
=\frac98\,\frac{(-1)^a}{((3a)!)^2}=\frac92.
\]
这证明 (AS.2)。R988(988.26) 已有
\(\overline{\mathcal G_{3(p-1)}}=-\beta^{-3}\)，故 (AS.3) 随即成立。
没有把 R973 表中的旧 B 字段当作原 \(c_{p-r}^{-}\)。

## 6. 对 O2 的实际范围

原高系数目标仍是 R988(988.23)–(988.24)：
\[
S_{\rm orig}\ne0
\ \Longleftrightarrow\
c_{p-r}^{\pm}\ne0
\ \Longleftrightarrow\
\mathcal F_{p-r}(0,-864)\ne0,
\]
其中 r=2 或 8，保原 p mod 12、p mod 9 分支。
(AS.2)–(AS.3) 只返回已知的固定低下标 3，未给这个随 p 增长的下标。

本次同时核读的两个来源也没有补齐该高坐标：

- Guerzhoy 的新论文 Theorem 1/3 研究固定权 2 整系数 newform。
  其 (11) 的 \(\mu_p\equiv-E_{p+1}/12=-\beta\) 是原低形式群坐标，
  已在 R984 的接口中登记；没有给原高 Artin–Hasse 坐标
  \(\gamma_1\) 或原 \(\mathcal F_{p-r}\) 的单位性。
- Hanson–Jameson Theorem 1 配合 Proposition 2/Table 1 的一维、平凡
  Nebentypus CM 空间只有
  \((k,N)=(2,27),(2,32),(2,36),(2,49),(4,9)\)。
  它不自动覆盖本题随 p 变化的高权输入，也没有指定原 r=8 的权 10 标量。

后继若用这些非零定理，必须另证原高源到相应实际系数的等式；
不能只凭同为 CM、同为 supersingular、Cartier 商一维或低晶体单位作替换。
本题原高近 p 值、同标签条件、全局高度及 O0 覆盖仍开放。

## 原始来源与审阅

- Scott Ahlgren and Detchat Samart,
  *A note on cusp forms as p-adic limits*,
  Journal of Number Theory 168 (2016), 360–373：
  [作者版全文](https://arxiv.org/pdf/1602.01036)，
  §4 的实际定义及 Proposition 4.2。
- Pavel Guerzhoy, Zachary A. Kent and Ken Ono,
  *p-adic coupling of mock modular forms and shadows*：
  [作者全文](https://uva.theopenscholar.com/files/ken-ono/files/125.pdf)，
  (1.12)、(3.5)、(3.6)。
- [NIST DLMF 16.4.5](https://dlmf.nist.gov/16.4#E5)：
  Dixon 终止求和的有限特化。
- Pavel Guerzhoy,
  *Non-vanishing of a certain quantity related to the p-adic coupling of mock modular forms with newforms*：
  [全文](https://arxiv.org/pdf/2506.07107)，Theorems 1/3、(11)–(12)。
- Michael Hanson and Marie Jameson, *Cusp forms as p-adic limits*：
  [作者全文](https://arxiv.org/pdf/2105.10444)，
  Theorem 1、Proposition 2、Table 1。

root 与 o2 分别核对原 q/eta 身份、Cartier 的负号与所有项、
Wilson/Dixon 有限和以及原 \(\beta\) 的 12 和模型符号。
外部定理只按以上实际假设使用；无新扫描，无旧有限窗口重算。
