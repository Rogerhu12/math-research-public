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
保全部原目标替换、输入哈希、真实 leading 方向和63个零配对。下面记录该下一系数的实际预读；它不替代六阶左方程的完整验证。


## 4. 已付五阶 jet 的三阶平方读数亦全部为零

在同一已付规范中，第三页的完整校正分为 $585$ 个目标校正行和末尾的一次横向 $QB$ 歧义行。令 $C_3\in\mathbb Q^{585\times12}$ 为其前 $585$ 行。第四页仅在三阶系数上增加一次横向的 $Q$ 列；第五页的相应歧义只改变四阶系数。因此七条实际五阶 jet 的准确三阶平方读数为
$$
\left(\lambda_{3,k}(n_j^2)\right)_{j,k}
=
\left(C_3|_{\{n_2^2,\ldots,n_{10}^2\}}\right)Z_4Z_5.
\tag{4.1}
$$
这里 $C_3$ 使用原第三页的全部 $1088$ 行校正身份，而非只取其低来源子集；第四、五页的 leading 矩阵保持原回执方向。

实际精确检查给
$$
\boxed{C_3|_{\{n_2^2,\ldots,n_{10}^2\}}=0_{9\times12},\qquad
\left(\lambda_{3,k}(n_j^2)\right)=0_{9\times7}.}
\tag{4.2}
$$
源码同时重新核对原二阶、三阶规范的完整身份及哈希，保留 §2 的九个平方目标替换和全部先前零读数；没有重复第四、第五页消元。

由于所有较低平方读数已经为零，原目标的下一可能系数为
$$
[s^6]\left(\lambda(s)^{\mathsf T}h_0(s)n_j^2\right)
=[s^3]h_0\,\lambda_3(n_j^2)=0.
\tag{4.3}
$$
这是七条固定五阶 jet 的已证系数读数。当前只知其左方程为 $O(s^6)$，尚未由本次读数证明它们具有六阶提升。若后续在这些固定 jet 的线性组合上完成六阶提升，且仅在五阶系数加入一次横向 $Q$ 歧义，则 (4.3) 保持为零，因此这一项也不会产生原目标的 $s^6$ 障碍。这里仍未声称完整成员性、所有五阶 jet 的结论或六阶可提升维数。

本次[小源码](../notes/2026-11-15-r150-zero-paid-fifth-jets-third-square-readout-789f.py) SHA256 为
~~~
bb8d2690a1ea74984c05a9863fb7607c87f414eeac2b20d5f5458ff6c9fe05c4
~~~
实际 run43702348535，step zero-fifth-third-square-readout，执行源码提交
f01c3f97500b3c9bc5b0a8a25e0f799eb97a3096；数学
4.211737646000074 秒，墙钟4.273404758000197秒，退出码0。

原 $9\times12$ 三阶平方读数 SHA256：
~~~
6c4cb68e82fa9e818fd1fa8a40f57c2ce3ac63e56774dfa00232b29b01b07ef3
~~~
七条 $9\times7$ 读数及乘 $[s^3]h_0$ 后的矩阵均为零，其 SHA256 均为
~~~
50781d98bb92faafbe14ada9db16b30b1c1142776f5cbfb941b73489f02829a6
~~~
完整临时回执4085字节，SHA256：
~~~
ed18d659840b5a90ed42f5caeb2073738846ff44ce5718e443e6723a5461a3c3
~~~
[实际小回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-fifth-third-square-readout.json)
保存输入身份、完整校正验证、两组实际读数及准确未提升范围。


## 5. 同一完整五阶截断的四、五阶平方读数也为零

为构建第六页，程序从同一实际第五页的四个临时 high/low 检查点读取完整数据，按原生产者 binding 验证后，重建七条固定五阶 cochain。所有先前规范哈希、全部原来源身份及 leading 方向保持；这一步没有新增连接秩结论。

令 $H_4,H_5\in\mathbb Q^{585\times7}$ 为重建后的实际四、五阶低目标系数。第五页加入四阶系数的 $QB$ 项只支持一次横向；三次横向目标部分不读二次平方坐标。因此源码直接取得完整系数而非部分代表，并精确得到
$$
\boxed{
\left(\lambda_{4,k}(n_j^2)\right)_{j,k}
=\left(\lambda_{5,k}(n_j^2)\right)_{j,k}
=0_{9\times7}.
}
\tag{5.1}
$$
结合先前全部系数，对每个固定第五页 cochain 有准确多项式恒等式
$$
\boxed{
\lambda_{\le5}(s)^{\mathsf T}n_j^2=0,\qquad
\lambda_{\le5}(s)^{\mathsf T}h_0(s)n_j^2=0
\quad(2\le j\le10).
}
\tag{5.2}
$$
这比仅报某个下一系数为零更明确，但仍然是固定截断的配对，不是完整左零向量或成员性证书。

若后续扩展保持此处零至五阶系数，或只加入已说明的不读平方坐标的一次横向歧义，则目标配对的首个新可能项来自
$$
s^9[s^3]h_0\,\lambda_6(n_j^2).
\tag{5.3}
$$
要把它用于否定成员性，仍须核实相应阶数的全部原左方程；不能只凭 (5.3) 的预读数作结论。允许改变更低 cochain 代表的其他分支，也不由本节自动覆盖。

实际 [cochain 准备源码](../notes/2026-11-15-r150-zero-paid-fifth-cochain-export-789f.py)
SHA256 为
~~~
f2e03d6c07e301c85f8c48358d4eefa2cdc201124b0cf32ca469c25005839fae
~~~
run43702348535，step zero-paid-fifth-cochain-export，执行源码提交
846daedbd85a3644a1b1bcccc48b7168de21d430；数学11.027009277000616秒，墙钟11.091623395999704秒，退出码0。四个 $9\times7$ 二至五阶读数的 SHA256 均为
~~~
50781d98bb92faafbe14ada9db16b30b1c1142776f5cbfb941b73489f02829a6
~~~
临时 $4738\times7$ 完整有理 cochain 包的规范矩阵 SHA256：
~~~
cf952faf51a2e17fe9b5d668ac8d9c171ce299d0d3a413e5808053640ce94640
~~~
完整临时小回执23197字节，SHA256：
~~~
6235424955208f4fdc7a22d995c3eaf54f8d37ed17badaaadd1413c5bba8bf7b
~~~
[已发表小记录](../notes/r150-infinity-remote-session-789f/43702348535-zero-paid-fifth-cochain-export.json)
保存实际四个阶段的读取身份、所有 cochain 分块哈希和四组零读数。完整可重算矩阵只保于同一临时工作会话。
