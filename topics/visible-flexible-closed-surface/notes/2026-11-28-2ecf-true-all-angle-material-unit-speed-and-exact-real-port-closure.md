# 新两类真实端口的全角弦预算与准确单位速材料连接

**准确有理与构造证明。** [R284](../results/R284-exact-unit-material-meridians-between-both-true-port-families.md) 对整个 R273、R282 端口参数矩形支付准确归一化材料角的全弦上界 .707486、同一真区间长度余量 >.0881882。98 个单位方向的凸包内球和严格正停留时间给出一张具体 C² 材料图，在全部 s,u 上准确 E=1，两边六 jets 逐函数接合。操作在原长度上完成；F、G、表面浸入/嵌入和 reach 还需另证。此处的确切构造和低曲率数值球向场各有自己的身份。
实际 R282 负端角输入完整重生 128 个移位角及 129 个材料径点。端位浮点自检最大 3.64e−15，速度范数、端速度和加速度亦已实际检查。初次全弦检程序用了错误的 NPZ 键名并退出1，改正为真 centralA、centralB 后得到下面完整连续证书。

## 可移植重生

W 含 R267 的真实 H65 master 和出口角图证书、R282 的全矩形预算以及配套 coast master。S 为公开课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 "$S/2ecf-polar-true-material-ports-all-chord-slack.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --graph polar-gap092-exit-graph.json --new-budget polar-returning-rigorous.json --output polar-R273-R282-all-material-slack-certified.json
python3 -u "$S/2ecf-polar-true-unit-material-fully-closed-meridians.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --slack polar-R273-R282-all-material-slack-certified.json --output polar-unit-material-exact-R282.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-true-material-ports-all-chord-slack.py | 536ed5fe8b1aad45e2efa45ccb8fa63dd1464a152b7a1ff9d36172c9cbed43d3 |
| 2ecf-polar-true-unit-material-fully-closed-meridians.py | 6898435c89da5a746022f9421990c467477030f2d4a305d911f9ed6d4ac34140 |
| polar-R273-R282-all-material-slack-certified.json | f00fc8a40608476e394fb7b0a7490931f0c79248db028a1a50d4b27bab680d2e |
| polar-unit-material-exact-R282.json | ef99bad93a3b7feacf937bc275f4756be3208397709f715641c67caeb96ced96 |
| polar-R273-R282-all-material-slack-exit.json | 6fdbf457cc911293dfaade43250326e17db3770db4cac73ab7a70459a57e676e |
| polar-R273-R282-all-material-slack-certified-exit.json | 4694ae9de597f7a2b1fd4009dbc7e8935f5a530fe293b6c8ae09ba5152ac016f |
| polar-R273-R282-all-material-slack-certified.log | e85fc8668644295ed2568b16bfff093c379aa4d1baced48c02739d00f9c02246 |
| polar-unit-material-exact-R282-exit.json | 5c8eb9c80d83a05110183e7fb78df4fbe197fbec5f878174c5df482a4a870d9a |
| polar-unit-material-exact-R282.log | 4cf2c2f0ee0f2ad708ee3c0e0e49cc999a6e426c09bfab8a15bcea07c58e7717 |
