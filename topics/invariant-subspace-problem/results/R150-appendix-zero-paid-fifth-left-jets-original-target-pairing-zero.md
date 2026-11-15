# R150：原九平方目标与已付零点五阶左延拓的完整配对为零

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿核定原目标和完整共动运输后，检查[零点十七条五阶左延拓](R150-appendix-zero-seventeen-fifth-left-jets-factor99-and-cost8634.md)能否否定原候选 $h_0t_j$ 的特征零来源归属。实际结果为全部九个目标、七条非恒等五阶 jet 的配对均为 $0\bmod s^6$。这给出该组已付左 jet 没有成员性障碍的准确结论，不证明目标已属于原像。

## 1. 原目标与候选的精确形式

[原九目标证明](R150-appendix-nine-original-targets-exact-mod31-annihilator-degree24.md)及[原正常形生成器](../notes/2026-11-14-r150-native-normal-form-789f.cpp)给
$$
t_j(s,m)=\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2,
\qquad 2\le j\le10.
\tag{1.1}
$$
它是平方目标，不是一次横向变量。primitive 十七式的非零常数行缩放只改变来源列，不给目标增加缩放。

代入同一完整共动关系
$$
m_a=\sum_{r=0}^a\binom ar s^{a-r}n_r
$$
并使用
$$
\sum_{a=r}^j\binom ja(-1)^{j-a}\binom ar=\mathbf1_{r=j},
$$
得到准确恒等式
$$
\boxed{t_j(s,m(s,n))=n_j^2.}
\tag{1.2}
$$
若 $A_{\rm new}=T A_{\rm old}V_{\rm src}$，目标亦乘同一 $T$，左泛函按 $T^{\mathsf T}$ 运输。因此 (1.2) 与原目标配对完全一致，没有仅运输方程而漏掉目标。

[原整数模型](../notes/2026-11-14-r150-ninth-first-integer-model-789f.py)保
$$
h_0=s^3(s-2)F_+^2F_-^2E_8,
$$
其中 $F_+(0)=-8$、$F_-(0)=864$、$E_8(0)=9600$。故
$$
v_0(h_0)=3,\qquad [s^3]h_0=-917294284800\ne0.
\tag{1.3}
$$

## 2. 只需读取已付二阶校正的九个平方坐标

设实际五阶左 jet 为
$$
\lambda(s)=\sum_{k=0}^5s^k\lambda_k,\qquad
A(s)^{\mathsf T}\lambda(s)=O(s^6).
$$
其 $\lambda_0,\lambda_1$ 最高一次横向，故与 $n_j^2$ 配对为零。于是
$$
\lambda(s)^{\mathsf T}(h_0t_j)
=s^5[s^3]h_0\,\lambda_2(n_j^2)\pmod{s^6}.
\tag{2.1}
$$

原十三条二阶基由十条纯方向和三条一次横向方向组成。前十条的二阶校正只支持一次横向。令 $H_{\rm normal}$ 为已付 $1088\times595$ 完整二阶规范中的 $585\times3$ 实际校正。原第三、四、五页的 leading 矩阵分别为
$$
Z_3\in\mathbb Q^{13\times12},\qquad
Z_4\in\mathbb Q^{12\times9},\qquad
Z_5\in\mathbb Q^{9\times7}.
$$
三者均逐哈希对应实际已发表回执。第三页对 $\lambda_2$ 的 $QB$ 修改仅支持一次横向；第四、五页的相应歧义分别修改 $\lambda_3,\lambda_4$。因此准确有
$$
\left(\lambda_{2,k}(n_j^2)\right)_{j=2,\ldots,10;\ k=1,\ldots,7}
=
\left(H_{\rm normal}|_{n_j^2}\right)
\left(Z_3Z_4Z_5\right)_{\{10,11,12\},:}.
\tag{2.2}
$$
下标10、11、12为零起算。源码重建原二阶矩阵，核对全部1088行及完整规范哈希，再读取小回执中的三层 leading；没有重算第三至第五页消元。

实际精确有理乘回给
$$
\boxed{H_{\rm normal}|_{\{n_2^2,\ldots,n_{10}^2\}}=0_{9\times3},}
$$
$$
\boxed{\left(\lambda_{2,k}(n_j^2)\right)=0_{9\times7}.}
\tag{2.3}
$$
另十条恒等纯泛函沿全参数也杀掉这些平方目标。所以全部十七条已付五阶左 jet 均给
$$
\boxed{\lambda(s)^{\mathsf T}(h_0t_j)=0\pmod{s^6}
\quad(2\le j\le10).}
\tag{2.4}
$$

## 3. 准确范围与实际记录

(2.4) 不证明 $h_0t_j\in\operatorname{im}_{\mathbb Q[s]}A$，也不证明所有五阶左 jet 都给零。它只说明这十七条真实已付延拓没有产生预期的局部否定证书。

若某一已付左 jet 的 (2.1) 非零，确会排除完整6188来源模块中任意参数次数的有理多项式表示，且31分母不能改变该特征零否定；本次实际并未发生这种情况。完整理想中更高 $m$ 次数来源也不在此检验的断言范围。

[小源码](../notes/2026-11-15-r150-zero-paid-fifth-jets-original-target-pairing-789f.py)
SHA256为
~~~
003ea764ed53fd8b04dc5254f50e48f48dcf3934d640c396465a38d9f2a53b13
~~~
实际run43702348535，step zero-fifth-original-target-pairing，执行源码提交
a2d02e47c7a380ed6afe806f3ce82a9567ea0305。20秒共享预算、512MiB；
实际数学1.5095971929999905秒，墙钟1.5671418279998761秒，退出码0。

$9\times3$ 原配对SHA256：
~~~
bbc4d48ba43feb38f601eccea7cc8bba168f7c3f844630694f2d4cb08353243d
~~~
$9\times7$ 实际五阶配对SHA256：
~~~
50781d98bb92faafbe14ada9db16b30b1c1142776f5cbfb941b73489f02829a6
~~~
完整临时小回执3394字节，SHA256：
~~~
a952b3cbff00dd963f2c9198da07d07bc5ba170597fe26de358e4c6f4f424d7b
~~~
[已推记录](../notes/r150-infinity-remote-session-789f/43702348535-zero-fifth-original-target-pairing.json)
保全部原目标替换、输入哈希、真实 leading 方向和63个零配对。下一潜在目标系数为 $\lambda_3(n_j^2)$；只有连同真实六阶延拓后，才能作为 $s^6$ 成员性障碍使用。
