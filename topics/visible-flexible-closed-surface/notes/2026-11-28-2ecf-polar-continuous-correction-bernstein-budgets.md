# 强幅度完整 Cartesian 修正场的连续 Bernstein 两/三jet预算

日期：2026-11-28。状态：**对明确已保存修正场W的严格有理连续界；不含背景X，不是总metric/曲率/reach证书**。实际消费暖3、暖20的全部12789个系数和权威physicalKnots，对全部54个闭径向span和所有实角证明下列界；两个独立进程均自然退出0。

## 准确定义与证明

入口 `2ecf-polar-c2-correction-bernstein-budget.py` 把JSON保存的有限binary64系数和物理knots逐个解释为相应的精确二进有理数；不使用仅供展示的normalizedBreaks。87个完整自由径向行外补两端各三个零行，共93个五次B样条控制行，角通道为三Cartesian分量×(1+2×24)=147。

采用已发表 `6a65-m12-local-bernstein-angular-metric-budget.py` 的 exact Boehm单结插入，将每个内结精确增至重数5；原实多项式场不变。每一物理span [a,b] 的6个Bernstein控制行记为c_j。对h=b−a及0≤r≤3，连续片内径向r阶导控制行由准确公式

$$c_j^{(r)}=\frac{5!}{(5-r)!h^r}\Delta^r c_j$$

给出。真实Fourier通道为e_ℓ cos(ku)或e_ℓ sin(ku)，其q阶角导绝对值≤k^q，q=0时常数通道的0^0取1。Bernstein基在闭span非负且和为1，因此对任意实角u和径向s都有

$$\|\partial_s^r\partial_u^q W(s,u)\|_2\leq \max_j\sum_\nu |c_{j,\nu}^{(r)}| k_\nu^q,\qquad r+q\leq3.$$

右侧全由有理四则运算构成，最终向上舍入到96位二进有理网格；准确上界分数在原始报告中。该证明包括所有角、全部span、全部端点，不用有限采样外推。逐内结准确比对两侧0/1/2阶导控制端点，相等检查全部通过；两端0/1/2阶迹严格为0。于是W作零延拓为C2。第三径向导可能跨结跳跃，只对两侧闭片分别给界；由于Wss连续，该全片界也控制Wss沿s的全局Lipschitz常数。

这些是存储系数定义的数学修正场的界，不是其所有浮点B样条/三角求值的舍入误差界。更没有把背景极性逆图的浮点值提升为准确连续场证明。

## 两个实际完整场

| 导数 | 暖3连续上界（保守向上十进制） | 暖20连续上界（保守向上十进制） |
| --- | ---: | ---: |
| W | 0.570765 | 0.554147 |
| Wu | 2.562689 | 2.189612 |
| Wuu | 22.331633 | 17.992059 |
| Wuuu | 329.923459 | 204.047297 |
| Ws | 6.114844 | 10.585176 |
| Wsu | 43.377426 | 67.723209 |
| Wsuu | 566.141049 | 785.164510 |
| Wss | 7063.684343 | 10115.893214 |
| Wssu | 55914.022973 | 73145.761465 |
| Wsss | 10743310.864847 | 16063047.746007 |

暖3进程自然退出0/2.621130836秒，暖20自然退出0/6.174353756秒；峰值子进程RSS均33232 KiB。比较上界大小本身不证明真实sup相同方向变化；真实漏峰的恶化已有独立G3同场观察单独证明。这一全域预算说明旧G2有限样本不能控制非常大的径向导数，未来密模型/连续核必须消费实际W及背景预算。

例如暖20的Wsss全域上界约1.6063×10^7，单靠这个粗界和稀节点间距不能得到足够小的Wss插值误差；它不构成当前曲率已经受控的证明。新958节点G10计算和G11真实空间观察仍在继续。

## 实际命令与复核

```sh
python3 "$WORK/2ecf-polar-c2-correction-bernstein-budget.py" \
  --scripts "$SCRIPTS" --state "$WORK/polar-c2-step03-step01-state.json" \
  --output "$WORK/polar-c2-warm03-exact-correction-budget.json"
```

暖20仅替换实际state和输出文件名。全部原始exact分数/54片预算留临时区。

| 源码/实际输入/实际输出 | SHA-256 |
| --- | --- |
| `2ecf-polar-c2-correction-bernstein-budget.py` | `2535060ad754eac09199a1c8eaab0a2456dd97805c80de95ec52791a7da86c8a` |
| `polar-c2-step03-step01-state.json` | `9b224ebd1ec7da59291ea96141316469cf07c437499b5813cdcccdc66abdc530` |
| `polar-c2-step20-step01-state.json` | `89dc1453a1ad897b1d48958a505e7042988bac29eceff7928f67484b879522ad` |
| `polar-c2-warm03-exact-correction-budget.json` | `f9da0f789926cfb383f6caaf2e037a3a8e236a9f9306a1067c28e33d40839f1a` |
| `polar-c2-warm03-exact-correction-budget-exit.json` | `cb38d66588c6c329c287cd2544abfb5974ab56fcaa5c3a995eec1ffc4393a98a` |
| `polar-c2-warm20-exact-correction-budget.json` | `6680b9fd038e506b09c0cbc955419842acfb75bc912b72060c6c0218cc84b4c3` |
| `polar-c2-warm20-exact-correction-budget-exit.json` | `abbd9e497acf8838cf9ba2b4b24a568b91f5f95638369600b217dedd2df419fe` |
