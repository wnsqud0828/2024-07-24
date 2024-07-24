import streamlit as st
st.title('나의 첫 번째 웹서비스!')
name = st.text_input('이름을 입력해 주세요 : ')
menu = st.selectbox('좋아하는 음식을 선택하세요!', ['망고 빙수', '쿠키앤크림', '이상한 나라의 솜사탕'])
if st.button('인사말 생성'):
  st.write(f'안녕하세요! {name}님! 당신이 좋아하는 음식은 {menu}이군요! 너무 맛있겠어요! 반갑습니다! :)')
  
