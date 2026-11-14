# 大素因子本身的分裂类：已付范围与精确加权缺项

日期：2026-11-12。状态：以下剩余类、现成定理的适用范围及条件化归约已核实；
尚未证明同时有 $u<\sqrt p$ 与指定分裂类的无穷性。
本篇不修改 R126 的无条件结论，也不把正密度集合与任意无穷集合相交。

## 1. 本题准确需要的类

对 $p\nmid30$，
$$
 p\text{ 在 }\mathbb Q(i),\mathbb Q(\sqrt{-15})\text{ 均分裂}
 \iff p\bmod60\in\mathcal H:=\{1,17,49,53\}.
 \tag{1}
$$
证明是 $p\equiv1\pmod4$ 与
$\chi_{-15}(p)=(p/3)(p/5)=1$；后者在模 $15$ 的
$\{1,2,4,8\}$ 上成立。四类占全部素数密度 $1/4$。

R126 先选 $\ell\equiv-1\pmod B$，再令
$p=P^+(\ell+1)>x^{667/1000}$。它付清的是 **$\ell$ 的固定进程**。
由 $B\mid\ell+1$、$(p,B)=1$ 得 $B\mid u=(\ell+1)/p$；
这不指定 $p\bmod60$。即使增大固定 $B$，同一推论仍只限制 $u$
的整除性。

## 2. 可合法限制输入 $p$ 类的较弱无条件定理

Banks--Shparlinski（2007），Theorem 1.1，以及 Wu（2019），
Theorem 1.1，证明对每个固定
$$
 \frac{32}{17}<\eta<2
$$
和固定非零移位 $a$，除 $O_A(X/(\log X)^A)$ 个输入素数
$p\le X$ 外，存在素数 $\ell\asymp p^\eta$，使
$p=P^+(\ell-a)$。取 $a=-1$。

由于例外集在全部素数中为密度零，确可再要求 (1)；这是
密度一集合与一个固定正密度类的合法相交。固定附加条件
$\ell\equiv-1\pmod B$ 可直接使用 R110 已核的 Mikawa
平均模数定理，取模数 $Bp$；例外数量仍为
$O_{A,B}(X/(\log X)^A)$。这里不是把 Banks--Shparlinski
打印的定理擅自添加第二个条件。

然而这些结论只给
$$
 u\asymp p^{\eta-1},\qquad \eta-1>\frac{15}{17}.
 \tag{2}
$$
它们没有给 $u<\sqrt p$。R126 的 $\vartheta>2/3$ 则给
$u\ll p^{(1-\vartheta)/\vartheta}=p^{333/667}$，
但没有给 (1)。两者的量词不能拼接成同时成立的结论。

## 3. Fouvry 加权论证若保大因子类，准确还缺什么

令 $60\mid B$ 固定，并记
$$
 \pi_B(x;q)=\#\{\ell\le x:\ell\text{ 素},\
                 \ell\equiv-1\pmod B,\ q\mid\ell+1\}.
$$
只对 $(q,B)=1$ 的素数求和。定义
$$
 T_{\mathcal H}(x)=
 \sum_{\substack{\ell\le x\ \ell\equiv-1\ (B)}}
 \sum_{\substack{q^v\mid\ell+1\ v\ge1\\
                  q\text{ 素},\ (q,B)=1,\ q\bmod60\in\mathcal H}}
                  \log q.
 \tag{3}
$$
固定素因子与高次幂的误差，与 R126 §1 相同为 $o_B(x)$。
因此
$$
 T_{\mathcal H}(x)=
 \sum_{\substack{q\text{ 素},\ (q,B)=1\\q\bmod60\in\mathcal H}}
                \pi_B(x;q)\log q+o_B(x).
 \tag{4}
$$

**准确的条件化归约。** 若另外证明
$$
 T_{\mathcal H}(x)=\left(\frac14+o_B(1)\right)
                       \frac{x}{\varphi(B)},
 \tag{5}
$$
则 R126 的论证给
$$
 \#\{\ell\le x:\ell\equiv-1\pmod B,\
 p=P^+(\ell+1)>x^{667/1000},\ p\bmod60\in\mathcal H\}
             \gg_B x/\log x.
 \tag{6}
$$
这里 (5) 是附加输入，当前没有证明。

具体地，Bombieri--Vinogradov 在 $q\le x^{1/2}$ 的主项，
加上模 $60$ 素数定理，为 $x/(8\varphi(B))+o_B(x)$。
Fouvry 的异常模数集限制到 $\mathcal H$ 不会变大，故其中段上界为
$$
 \frac{x}{4\varphi(B)}
       \int_{1/2}^{667/1000}C(t)\,dt+o_B(x).
$$
R126 的纯有理证书给该积分 $<0.498641$。从 (4)--(5) 相减得
$$
 \sum_{\substack{q>x^{667/1000}\\q\bmod60\in\mathcal H}}
           \pi_B(x;q)\log q
 \ge\frac{x}{4\varphi(B)}
          (0.5-0.498641-o_B(1)),
 \tag{7}
$$
从而得到 (6)。所以把固定类加进 **已知中段上界** 没有难度；
缺的是 (5) 的全范围总量，而不是该处的主项密度。

为把缺项写成三个准确的角色和，对
$\chi\in\{\chi_{-4},\chi_{-15},\chi_{60}\}$ 定义
$$
 T_\chi(x)=\sum_{\substack{\ell\le x\ \ell\equiv-1\ (B)}}
      \sum_{\substack{q^v\mid\ell+1\ v\ge1\\q\text{ 素},\ (q,B)=1}}
                    \chi(q)\log q.
 \tag{8}
$$
由
$1_{\mathcal H}(q)=\frac14(1+\chi_{-4}(q))(1+\chi_{-15}(q))$
及 $\chi_{-4}\chi_{-15}=\chi_{60}$，有
$$
 T_{\mathcal H}(x)=\frac14\left(
 \frac{x}{\varphi(B)}+T_{\chi_{-4}}(x)+T_{\chi_{-15}}(x)
                         +T_{\chi_{60}}(x)\right)+o_B(x).
 \tag{9}
$$
完整的对数恒等式只支付第一项。三个非平凡角色和各为 $o_B(x)$
是 (5) 的一个充分条件；在现已核的来源里，没有找到这一附加输入。
此处不把文献检索的范围陈述成普遍的不存在定理。

## 4. 较强指数的来源也不能直接支付 (5)

Fouvry（1985）§VI，pp.404--406，以
$\sum_\ell\log(\ell+1)\sim x/\varphi(B)$ 为起点，扣除小、中素因子。
Baker--Harman（1998）§7，印刷 p.356，式 (7.1)--(7.4)，把目标改进
明确归约为
$$
 \sum_{x^{1/2}<q\le x^{0.677}}\pi(x;q,a)\log q
                  <(1/2-3\epsilon)x.
$$
它仍改进同一中段上界，并未在这个论证中建立 (8) 的全范围消去。
因此不能只在该和的索引加 $q\in\mathcal H$，随后仍使用未加权
$\log(\ell+1)$ 的全部主项。

本题当前可同时使用的两种已付输入是：

- R126：$u=o(\sqrt p)$，但没有给变化 $p$ 的分裂类；
- R110 的密度一版本：可以指定 (1)，但只有 (2) 的余因子范围。

R135 的目标 CL reciprocity 函数总次数为 $O(p)$，需要目标 $E$
普通；源 CL 点又需要 $p$ 在 $F$ 分裂。故若后续几何论证同时
要求 $u<\sqrt p$，必须另外支付 (6) 或绕过该大小条件。

## 原始来源

1. É. Fouvry（1985），*Théorème de Brun--Titchmarsh; application au
   théorème de Fermat*，Invent. Math. **79**, 383--407，尤其 §VI。
   <https://doi.org/10.1007/BF01388980>。
   固定进程及勘误已在 R126 逐段核对。
2. R. C. Baker、G. Harman（1998），*Shifted primes without large prime
   factors*，Acta Arith. **83**, 331--361，Theorem 2、§7。
   <https://matwbn.icm.edu.pl/ksiazki/aa/aa83/aa8342.pdf>。
3. W. D. Banks、I. E. Shparlinski（2007），*On values taken by the
   largest prime factor of shifted primes*，J. Aust. Math. Soc. **82**,
   133--147，Theorem 1.1。
   <https://www.austms.org.au/Publ/JAustMS/V82P1/pdf/c119.pdf>。
4. J. Wu（2019），同名论文，J. Aust. Math. Soc. **107**, 133--144，
   Theorem 1.1。改进的是允许 $\eta$ 的上端，所需下端仍为 $32/17$。
   <https://doi.org/10.1017/S144678871800023X>。
